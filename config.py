import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '4620')  # Use default secret key for development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/yourdatabase')  # Update for your database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')  # Define the upload folder
    MAX_CONTENT_LENGTH = 150 * 1024  # Limit upload size to 150 KB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Define allowed file extensions

class ProductionConfig(Config):
    DEBUG = False  # Disable debugging in production
    TESTING = False  # Disable testing mode in production

class DevelopmentConfig(Config):
    DEBUG = True  # Enable debugging in development
    TESTING = True  # Enable testing mode in development
