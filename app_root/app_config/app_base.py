from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore
from os import path
import logging.config
from app_root.api import get_blueprint as get_api_blueprint
from app_root.app.views.home import bp_home
from app_root.core.auth import get_login_manager
from app_root.core.auth.encryption import EncryptionService
from app_root.core.data_model import db
from app_root.core.data_model.auth import User, Role
from app_root.core.schemas import jsonschema_dir

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)
basedir = path.abspath(path.dirname(__file__))


class AppBase(object):

    def __init__(self, config):
        self.app_instance = self.init_app(config)

    def __call__(self, environ, start_response):
        return self.app_instance(environ, start_response)

    def init_app(self, config):
        app = Flask(__name__)
        app.config.from_object(config)
        config.init_app(app)
        self.init_database(app)
        self.register_blueprints(app)
        app.config['JSONSCHEMA_DIR'] = jsonschema_dir
        # register_other_things(app)

        return app

    def register_blueprints(self, app_instance):
        app_instance.register_blueprint(bp_home, url_prefix='/')
        app_instance.register_blueprint(get_api_blueprint(), url_prefix='/api')

    def register_security(self, app_instance):
        user_datastore = SQLAlchemySessionUserDatastore(db, User, Role)
        security = Security(app_instance, user_datastore)
        security.init_app(app_instance, user_datastore)
        login_manager = get_login_manager()
        login_manager.init_app(app_instance)
        EncryptionService().init_app(app_instance)

    def init_database(self, app_instance):
        db.init_app(app_instance)
