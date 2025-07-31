from flask import Blueprint, send_from_directory, current_app


app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def homePage():
    return send_from_directory(current_app.static_folder, "index.html")