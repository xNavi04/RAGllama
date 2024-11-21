from flask import render_template, jsonify, request
from werkzeug.utils import secure_filename
import os
from assistant import ChatLLama

def init_routes(app):
    chat_llama = ChatLLama()

    @app.route('/')
    def index():
        template = "index.html"
        return render_template(template)
    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.get_json()
        prompt = data['message']
        if chat_llama.get_is_file():
            context = chat_llama.retrieve_embeddings(prompt=prompt)
            prompt = f'Użytkownik: {prompt} \nKotekst z embeddings: {context}'
        else:
            prompt = f'Użytkownik: {prompt}'

        assistant_response = chat_llama.stream_response(prompt=prompt)

        return jsonify({'response': assistant_response})
    @app.route('/upload-pdf', methods=['POST'])
    def upload_pdf():
        if 'pdf' not in request.files:
            return jsonify({'success': False, 'message': 'No file part'})

        file = request.files['pdf']
        if file.filename == '':
            return jsonify({'success': False, 'message': 'No selected file'})

        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Process the PDF and create embeddings
            text = chat_llama.get_text_from_pdf(filepath)
            chunks = chat_llama.split_text_into_chunks(text)
            chat_llama.create_vector_db_for_file_text(chunks)

            chat_llama.file = True

            return jsonify({'success': True})

        return jsonify({'success': False, 'message': 'Invalid file type'})