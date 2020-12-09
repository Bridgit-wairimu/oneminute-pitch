import os

class Config:
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY="hello"


    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "kirikabridgit@gmail.com"
    MAIL_PASSWORD = "90892000"

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/pitch'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:bridgit@localhost/pitch'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}