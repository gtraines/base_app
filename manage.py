import sys
from app_root.app_config.settings import configs
from app_root.app_config.app_base import AppBase
from app_root.core.data_model import db
from app_root.core.data_model import reset_database


def init_db(app_config):
    app_instance = AppBase(app_config).app_instance
    with app_instance.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........

        db.init_app(app_instance)
        reset_database(db, app_config)


def main():
    init_db(configs[sys.argv[1]])


if __name__ == "__main__":
    main()

