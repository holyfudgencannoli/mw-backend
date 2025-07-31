from flask import Flask
from flask_cors import CORS
from .static.static import app_bp




def create_app():
    app = Flask(__name__, static_folder='../frontend/dist', static_url_path='')
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    app.register_blueprint(app_bp)

    # Base.metadata.create_all(bind=engine)

    return app