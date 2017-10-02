from os import path
import logging.config
from flask_bootstrap import Bootstrap

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)
basedir = path.abspath(path.dirname(__file__))
bootstrap = Bootstrap()

