"""
Configuration class for Flask app settings.
Reads values from environment variables and sets defaults for development. 
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Central config class for Flask application.
    Values can be adjusted via environment variables or edited directly.
    """
    SECRET_KEY = os.getenv("SECRET_KEY","dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL","sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False