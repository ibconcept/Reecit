#config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '4620')  # Use default secret key for development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:kalamashaka@localhost/receipts')  # Use the correct environment variable
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking

class ProductionConfig(Config):
    DEBUG = False  # Disable debugging in production
    TESTING = False  # Disable testing mode in production

class DevelopmentConfig(Config):
    DEBUG = True  # Enable debugging in development
    TESTING = True  # Enable testing mode in development
