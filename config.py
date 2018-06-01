import os

class Config:
    SECRET_KEY = 'hihi'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/bookreviewsystem'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}