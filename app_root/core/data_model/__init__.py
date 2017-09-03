from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database(db_instance):
    import app_root.core.data_model.models
    import app_root.core.data_model.auth

    db_instance.drop_all()
    db_instance.create_all()
