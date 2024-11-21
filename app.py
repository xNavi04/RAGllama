import os
from config import create_app
from routes import init_routes

app = create_app()
init_routes(app)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
