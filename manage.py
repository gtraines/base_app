from app_root.app_config import settings
from app_root.core.data_model import db
from app_root.core.data_model import reset_database
from app_start import app


def init_db():
    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
        db.init_app(app)
        reset_database(db)


