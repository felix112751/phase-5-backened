import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    os.getenv('SECRET_KEY') #Used for session management and security