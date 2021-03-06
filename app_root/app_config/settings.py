import os


class AppSettings(object):
    STATIC_FOLDER = '../public'

    SECURITY_BLUEPRINT_NAME = 'auth'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'super-secret'
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    BCRYPT_LOG_ROUNDS = 24
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'your-gmail-username'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or'your-gmail-password'
    DEFAULT_MAIL_SENDER = 'info@site.com'

    CORE_DB_USER = os.environ.get('CORE_DB_USER') or 'root'
    CORE_DB_PASSWORD = os.environ.get('CORE_DB_PASSWORD') or 'password'
    CORE_DB_URI = os.environ.get('CORE_DB_URI') or 'localhost:3306'
    CORE_DB_NAME = 'basketdevilcore'

    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False

    SERVER_NAME = os.environ.get('FLASK_SERVER_NAME')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + CORE_DB_USER + ':' + CORE_DB_PASSWORD + \
                              '@' + CORE_DB_URI + '/' + CORE_DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentAppSettings(AppSettings):
    STATIC_FOLDER = '../../public'
    SERVER_NAME = 'localhost:8888'
    CORE_DB_USER = 'root'
    CORE_DB_PASSWORD = 'Mallory'
    CORE_DB_URI = 'localhost:3306'
    CORE_DB_NAME = 'basketdevilcore'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + CORE_DB_USER + ':' + CORE_DB_PASSWORD + \
                              '@' + CORE_DB_URI + '/' + CORE_DB_NAME
    DEBUG = True  # Do not use debug mode in production


class ProductionAppSettings(AppSettings):
    DEBUG = False

configs = {
    'development': DevelopmentAppSettings,
    'production': ProductionAppSettings
}

