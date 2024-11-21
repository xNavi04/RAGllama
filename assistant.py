import ollama
import chromadb
from pypdf import PdfReader

class ChatLLama:
    """
    A class to interact with a chat assistant powered by AI, specifically designed to
    respond to user queries and manage conversations.

    Attributes:
        file (bool): Indicates whether a file has been processed.
        client (chromadb.Client): The client for the ChromaDB.
        convo (list): The conversation history.
    """

    def __init__(self):
        """
        Initializes the ChatLLama instance, setting up the conversation history and
        system prompt for the assistant.
        """
        self.file = False
        self.client = chromadb.Client()
        self.convo = []

        system_prompt = (
            'Jesteś asystentem AI o imieniu Bartek. Jestes przeznaczony do odpowiadania użytkownikowi. Nie gadaj niepotrzebnych informacji. Staraj się tylko konieczne wypowiadać.',
            'Jezeli będzie chciał z Tobą pogadać na ogólne pytania, to też z nim pogadaj. Staraj się być towarzyski, ale któtko pisz.'
            'Bardszo ważne jest to, że odpowiedzi powinny być krótkie i zwięzłe. Staraj się tylko wypowiedzieć kluczowe informacje.',
            'Bierz pod uwagę dialog, jaki prowadziłeś z użytkownikiem.',
            'Twoje wypowiedzi muszą być poprawnie gramatycznie w języku polskim.'
        )

        for i in system_prompt:
            self.convo.append({'role': 'system', 'content': i})

    def stream_response(self, prompt):
        """
        Streams a response from the assistant based on the provided prompt.

        Args:
            prompt (str): The user prompt to which the assistant should respond.

        Returns:
            str: The assistant's complete response after streaming.
        """
        self.convo.append({"role": "user", "content": prompt})
        response = ''
        stream = ollama.chat(model="mistral", messages=self.convo, stream=True)
        print("\nAssistant")

        for chunk in stream:
            content = chunk["message"]["content"]
            response += content
            print(content, end='', flush=True)
        self.convo.append({"role": "assistant", "content": response})
        return response

    def create_vector_db_for_file_text(self, chunks):
        """
        Creates a vector database from the provided text chunks.

        Args:
            chunks (list): A list of text chunks to be added to the vector database.
        """
        vector_db_name = 'file_text'
        try:
            self.client.delete_collection(name=vector_db_name)
        except ValueError:
            pass

        vector_db = self.client.create_collection(name=vector_db_name)
        num = 0
        for chunk in chunks:
            serialized_convo = f'context: {chunk}'
            response = ollama.embeddings(model='nomic-embed-text', prompt=serialized_convo)
            embedding = response['embedding']

            vector_db.add(
                ids=[str(num)],
                embeddings=[embedding],
                documents=[serialized_convo]
            )
            num += 1

    def retrieve_embeddings(self, prompt):
        """
        Retrieves the best matching document from the vector database based on the
        provided prompt.

        Args:
            prompt (str): The prompt to embed and query against the vector database.

        Returns:
            str: The best matching document from the vector database.
        """
        self.file = True

        response = ollama.embeddings(model='nomic-embed-text', prompt=prompt)
        prompt_embedding = response['embedding']

        vector_db = self.client.get_collection('file_text')

        results = vector_db.query(query_embeddings=[prompt_embedding], n_results=1)

        best_embedding = results['documents'][0][0]

        return best_embedding

    def get_is_file(self):
        """
        Checks if a file has been processed.

        Returns:
            bool: True if a file has been processed, False otherwise.
        """
        return self.file

    @staticmethod
    def split_text_into_chunks(text, chunk_size=150, overlap=50):
        """
        Splits the input text into chunks of specified size with a specified overlap.

        Args:
            text (str): The text to be split into chunks.
            chunk_size (int, optional): The size of each chunk. Default is 100.
            overlap (int, optional): The number of overlapping words between chunks. Default is 50.

        Returns:
            list: A list of text chunks.
        """
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size - overlap):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks

    @staticmethod
    def get_text_from_pdf(path):
        """
        Extracts text from a PDF file.

        Args:
            path (str): The path to the PDF file.

        Returns:
            str: The extracted text from the PDF.
        """
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + " "
        return text
