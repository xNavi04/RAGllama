from flask import Flask
import os

endpoint_secret = "kdsjf98usddvbkjlwesadvkjadsd7sdv3evjk3evjn3lekvjn"

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", endpoint_secret)
    app.config["UPLOAD_FOLDER"] = "uploads"

    return app