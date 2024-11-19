from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(_name_)
    app.config.from_object('config.Config')  # Load config from config.py
    
    db.init_app(app)   # Initialize the database with the app
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    from .routes import main  # Import routes
    app.register_blueprint(main)  # Register routes blueprint

    return app
