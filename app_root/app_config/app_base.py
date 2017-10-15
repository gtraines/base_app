from os import path
import logging.config

from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore
from flask_bootstrap import Bootstrap
from flask_jwt import JWT

from app_root.api import get_blueprint as get_api_blueprint
from app_root.app.views.home import bp_home
from app_root.core.auth import jwt_handlers
from app_root.core.auth.login import LoginService
from app_root.core.auth.encryption import EncryptionService
from app_root.core.data_model import db
from app_root.core.data_model.auth import User, Role
from app_root.core.schemas import jsonschema_dir

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)
basedir = path.abspath(path.dirname(__file__))
bootstrap = Bootstrap()
jwt = JWT()


class AppBase(object):

    def __init__(self, config):
        self.app_instance = self.init_app(config)


    def __call__(self, environ, start_response):
        return self.app_instance(environ, start_response)


    def init_app(self, config):
        app = Flask(__name__, template_folder='../templates', static_folder='../../public')
        app.config.from_object(config)
        config.init_app(app)

        self.register_datasources(app)
        self.register_blueprints(app)
        self.register_plugins(app)

        return app
        
    def init_database(self, app_instance):
        db.init_app(app_instance)


    def register_blueprints(self, app_instance):
        app_instance.register_blueprint(bp_home, url_prefix='/')
        app_instance.register_blueprint(get_api_blueprint(), url_prefix='/api')

    def register_security(self, app_instance):
        user_datastore = SQLAlchemySessionUserDatastore(db, User, Role)
        
        security = Security(app_instance, user_datastore)
        security.init_app(app_instance, user_datastore)
        
        jwt_handlers.set_jwt_handlers(jwt)
        jwt.init_app(app_instance)

        LoginService().init_app(app_instance)
        EncryptionService().init_app(app_instance)


    def register_datasources(self, app_instance):
        app.config['JSONSCHEMA_DIR'] = jsonschema_dir
        db.init_app(app_instance)


    def register_plugins(self, app_instance):
        bootstrap.init_app(app_instance)
        
        

