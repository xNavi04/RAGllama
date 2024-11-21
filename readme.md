# **Technical Documentation for ChatLLama Application**

---

## 1. **Introduction**

The ChatLLama application is an interactive AI-powered chat assistant that allows users to have conversations, process PDF documents, and get answers to questions based on provided information. Through integration with various libraries, the application can generate responses, analyze text, and manage conversation history, offering concise and relevant answers.

---

## 2. **Requirements**

The following libraries are required for the application to function correctly:

- **Ollama**: For interaction with AI models and embeddings.
- **ChromaDB**: For managing the vector database.
- **PyPDF**: For extracting text from PDF files.
- **Flask**: For building web applications.
- **Werkzeug**: For secure file handling.
- **FastAPI**: For building the API.
- **Requests**: For making HTTP requests.
- **Numpy**: For numerical calculations.
- **Pydantic**: For data validation.
- **Starlette**: For managing asynchronous operations in Flask.
- **Uvicorn**: Server to run the application.

---

## 3. **Application Description**

The ChatLLama application consists of the `ChatLLama` class, which manages user interactions and text processing. Users can send queries to the assistant and upload PDF files, from which the application extracts text and creates vector databases for later retrieval.

### **Application Features:**

- **User Interaction**: Users can chat with the AI assistant, which responds based on conversation history and context.
- **PDF Processing**: Allows users to upload PDF files, extracts text, splits it into chunks, and creates embeddings for storage in the vector database.
- **Conversation History Management**: The application stores previous interactions, allowing for more context-based responses.

---

## 4. **Environment Setup**

Before running the application, it is necessary to create a virtual environment and install all dependencies. You can do this using `conda` or `pip`.

### **Steps:**

1. **Install Miniconda (if not already installed)**:
   - Download Miniconda from the [official page](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions.

2. **Create a new virtual environment**:
   - Open a terminal and run the following command to create a new environment (you can replace `myenv` with any name):
     ```bash
     conda create --name myenv python=3.11
     ```

3. **Activate the environment**:
   - Activate the created environment with the command:
     ```bash
     conda activate myenv
     ```

4. **Install all dependencies**:
   - Ensure you are in the active environment, then install the required packages. You can do this using the `requirements.txt` file (if it exists):
     ```bash
     pip install -r requirements.txt
     ```

5. **Deactivate the environment after finishing work**:
   - After you finish working in the environment, deactivate it with:
     ```bash
     conda deactivate
     ```

---

## 5. **Code Structure**

### Class: `ChatLLama`

#### Attributes:

- **file (bool)**: Indicates if a file has been processed.
- **client (chromadb.Client)**: Client for ChromaDB.
- **convo (list)**: Conversation history.

#### Methods:

- `__init__(self)`: Initializes the `ChatLLama` instance, sets conversation history and system messages.
- `stream_response(self, prompt)`: Sends a response from the assistant based on the given prompt.
- `create_vector_db_for_file_text(self, chunks)`: Creates a vector database from provided text chunks.
- `retrieve_embeddings(self, prompt)`: Retrieves the best-matching document from the vector database.
- `get_is_file(self)`: Checks if a file has been processed.
- `split_text_into_chunks(text, chunk_size=100, overlap=50)`: Splits text into chunks.
- `get_text_from_pdf(path)`: Extracts text from a PDF file.

### Flask Routes:

- **`/`**: Renders the main page.
- **`/chat`**: Handles user chat messages.
- **`/upload-pdf`**: Handles PDF file uploads and creates embeddings.

---

## 6. **Summary**

The ChatLLama application is a versatile tool for user interaction via chat, document processing, and generating context-based responses. By leveraging advanced technologies such as AI and vector databases, it provides an integrated and interactive user experience that can be applied in various scenarios, from technical support to education.

---










# **Dokumentacja Techniczna Aplikacji ChatLLama**

---

## 1. **Wprowadzenie**

Aplikacja ChatLLama to interaktywny asystent czatu wspierany przez sztuczną inteligencję, który pozwala użytkownikom na prowadzenie konwersacji, przetwarzanie dokumentów PDF oraz uzyskiwanie odpowiedzi na pytania w kontekście dostarczonych informacji. Dzięki integracji z różnymi bibliotekami, aplikacja może generować odpowiedzi, analizować tekst i zarządzać historią rozmów, oferując zwięzłe i trafne odpowiedzi.

---

## 2. **Wymagania**

Do prawidłowego działania aplikacji wymagane są następujące biblioteki:

- **Ollama**: Do interakcji z modelami AI i osadzeniami.
- **ChromaDB**: Do zarządzania bazą wektorową.
- **PyPDF**: Do wyodrębniania tekstu z plików PDF.
- **Flask**: Do tworzenia aplikacji internetowych.
- **Werkzeug**: Do bezpiecznego zarządzania plikami.
- **FastAPI**: Do budowania API.
- **Requests**: Do wykonywania zapytań HTTP.
- **Numpy**: Do obliczeń numerycznych.
- **Pydantic**: Do walidacji danych.
- **Starlette**: Do zarządzania asynchronicznymi operacjami w Flasku.
- **Uvicorn**: Serwer do uruchamiania aplikacji.

---

## 3. **Opis Aplikacji**

Aplikacja ChatLLama składa się z klasy `ChatLLama`, która zarządza interakcjami z użytkownikami oraz przetwarzaniem tekstu. Użytkownicy mogą przesyłać zapytania do asystenta, a także ładować pliki PDF, z których aplikacja wyodrębnia tekst i tworzy bazy wektorowe do późniejszego wyszukiwania.

### **Funkcje Aplikacji:**

- **Interakcja z użytkownikiem**: Użytkownicy mogą prowadzić rozmowy z asystentem AI, który odpowiada na ich pytania na podstawie historii rozmów i kontekstu.
- **Przetwarzanie PDF**: Umożliwia przesyłanie plików PDF, z których aplikacja wyodrębnia tekst, dzieli go na fragmenty i tworzy osadzenia do przechowywania w bazie wektorowej.
- **Zarządzanie historią rozmów**: Aplikacja zapamiętuje wcześniejsze interakcje, co pozwala na bardziej kontekstowe odpowiedzi.

---

## 4. **Konfiguracja Środowiska**

Przed uruchomieniem aplikacji konieczne jest utworzenie wirtualnego środowiska oraz zainstalowanie wszystkich zależności. Możesz to zrobić korzystając z `conda` lub `pip`.

### **Kroki:**

1. **Zainstaluj Miniconda (jeśli jeszcze go nie masz)**:
   - Pobierz Minicondę ze strony [oficjalnej](https://docs.conda.io/en/latest/miniconda.html) i postępuj zgodnie z instrukcjami instalacji.

2. **Utwórz nowe środowisko wirtualne**:
   - Otwórz terminal i uruchom poniższe polecenie, aby utworzyć nowe środowisko (możesz zastąpić `myenv` dowolną nazwą):
     ```bash
     conda create --name myenv python=3.11
     ```

3. **Aktywuj środowisko**:
   - Aktywuj utworzone środowisko poleceniem:
     ```bash
     conda activate myenv
     ```

4. **Zainstaluj wszystkie zależności**:
   - Upewnij się, że znajdujesz się w aktywnym środowisku, a następnie zainstaluj potrzebne pakiety. Możesz to zrobić, korzystając z pliku `requirements.txt` (jeśli taki istnieje):
     ```bash
     pip install -r requirements.txt
     ```

5. **Dezaktywuj środowisko po zakończeniu pracy**:
   - Po zakończeniu pracy w środowisku, możesz je dezaktywować:
     ```bash
     conda deactivate
     ```

---

## 5. **Struktura Kodu**

### Klasa: `ChatLLama`

#### Atrybuty:

- **file (bool)**: Wskazuje, czy plik został przetworzony.
- **client (chromadb.Client)**: Klient do ChromaDB.
- **convo (list)**: Historia rozmowy.

#### Metody:

- `__init__(self)`: Inicjalizuje instancję `ChatLLama`, ustawia historię rozmowy oraz systemowe komunikaty.
- `stream_response(self, prompt)`: Przesyła odpowiedź od asystenta na podstawie podanego zapytania.
- `create_vector_db_for_file_text(self, chunks)`: Tworzy bazę wektorową z podanych fragmentów tekstu.
- `retrieve_embeddings(self, prompt)`: Odzyskuje najlepszy dopasowany dokument z bazy wektorowej.
- `get_is_file(self)`: Sprawdza, czy plik został przetworzony.
- `split_text_into_chunks(text, chunk_size=100, overlap=50)`: Dzieli tekst na fragmenty.
- `get_text_from_pdf(path)`: Wyodrębnia tekst z pliku PDF.

### Trasy Flask:

- **`/`**: Renderuje stronę główną.
- **`/chat`**: Obsługuje wiadomości czatu użytkownika.
- **`/upload-pdf`**: Obsługuje przesyłanie plików PDF i tworzy osadzenia.

---

## 6. **Podsumowanie**

Aplikacja ChatLLama jest wszechstronnym narzędziem do interakcji z użytkownikami poprzez czat, przetwarzania dokumentów oraz generowania odpowiedzi na podstawie kontekstu. Dzięki wykorzystaniu zaawansowanych technologii, takich jak AI i bazy wektorowe, oferuje zintegrowane i interaktywne doświadczenie użytkownika, które może być stosowane w różnych scenariuszach, od wsparcia technicznego po edukację.

---
