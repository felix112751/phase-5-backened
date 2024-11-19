from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(_name_)
    app.config.from_object('config.Config')  
    
    db.init_app(app)   
    migrate.init_app(app, db)  

    from .routes import main  
    app.register_blueprint(main)  

    return app
