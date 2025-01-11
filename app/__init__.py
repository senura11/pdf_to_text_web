# app/__init__.py

from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Set configuration options
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB file size limit

# Import routes after the app is created
from app import routes