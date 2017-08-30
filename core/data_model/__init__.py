from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database(db_instance):
    from core.data_model.models import Post, Category  # noqa
    db_instance.drop_all()
    db_instance.create_all()
