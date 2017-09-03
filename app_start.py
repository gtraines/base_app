import logging.config

from app_root.api import get_blueprint as get_api_blueprint
from flask import Flask

# from base_app.app import get_blueprint as get_app_blueprint
from app_root.app_config import settings
from app_root.core.data_model import db

app = Flask(__name__)
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), './app_root/app_config/logging.conf')
logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    flask_app.register_blueprint(get_api_blueprint(), url_prefix='/api')
    #flask_app.register_blueprint(get_app_blueprint(), url_prefix='/')

    db.init_app(flask_app)

    return flask_app


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
