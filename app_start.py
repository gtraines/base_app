import logging.config
from os import path
from app_root.app_config.settings import DevelopmentAppSettings
from app_root.app_config.app_base import AppBase


def main():
    log_file_path = path.join(path.dirname(path.abspath(__file__)), './app_root/app_config/logging.conf')
    logging.config.fileConfig(log_file_path)
    log = logging.getLogger(__name__)
    log.info(DevelopmentAppSettings())
    app_base = AppBase(DevelopmentAppSettings)
    app = app_base.app_instance
    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=DevelopmentAppSettings.DEBUG)


if __name__ == "__main__":
    main()
