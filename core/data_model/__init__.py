from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database(db_instance):
    import core.data_model.models
    import core.data_model.auth

    db_instance.drop_all()
    db_instance.create_all()
