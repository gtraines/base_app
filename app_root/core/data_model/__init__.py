from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database(db_instance, app_config):
    from app_root.core.data_model import models
    from app_root.core.data_model import auth

    db_instance.drop_all()
    db_instance.create_all()