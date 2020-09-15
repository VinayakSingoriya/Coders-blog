import os
class Config:
    SECRET_KEY = '8c95cc7a49e1dacbec6ce1b28d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('mail_username')
    MAIL_PASSWORD = os.environ.get('mail_pass')
