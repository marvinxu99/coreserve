# app/config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey123456')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///coreserve.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', 'your-google-client-id')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', 'your-google-client-secret')
    SESSION_COOKIE_NAME = 'coreserve_session'  # Optional: Custom cookie name


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False