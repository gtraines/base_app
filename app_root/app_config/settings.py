
# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost:3306/dbschema'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Security Settings
SECRET_KEY = 'super-secret'
SECURITY_PASSWORD_SALT = 'super-secret'
