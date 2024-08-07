# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('you-will-never-guess') # 'SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_database.db'
    ENV = 'testing'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
