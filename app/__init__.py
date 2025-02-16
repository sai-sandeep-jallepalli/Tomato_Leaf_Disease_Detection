from flask import Flask
from flask_compress import Compress
from .config import CONFIG
import os

def create_app():
    
    app = Flask(__name__)
    
    app.config.update(CONFIG)
    
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    Compress(app)
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app