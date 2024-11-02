# app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base class
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey123456')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///coreserve.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', 'your-google-client-id')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', 'your-google-client-secret')
    SESSION_COOKIE_NAME = 'coreserve_session'  # Optional: Custom cookie name
    CACHE_TYPE = 'SimpleCache'  # Default cache type
    CACHE_DEFAULT_TIMEOUT = 900  # Default to 15 mins (for development)

class DevConfig(Config):
    DEBUG = True
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 900  # 15 mins for development

class ProdConfig(Config):
    DEBUG = False
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = 'redis://localhost:6379/0'
    CACHE_DEFAULT_TIMEOUT = None  # Never expires by default

class TestingConfig(Config):
    """Configuration for testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Use in-memory database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Choose the configuration based on an environment variable
config = {
    "development": DevConfig,
    "testing": TestingConfig,
    "production": ProdConfig,
}