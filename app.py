from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create Flask application instance
app = Flask(__name__)

# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the SQLite database with absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import data models (we'll create these next)
from data_models import db, Author, Book

# Initialize the database with the Flask app
db.init_app(app)