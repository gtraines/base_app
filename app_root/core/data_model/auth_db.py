from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


'''
import all modules here that might define models so that
they will be registered properly on the metadata.
Otherwise, you will have to import them first before calling
init_db()
'''
def init_db(app_config):
    from . import auth
    engine = create_engine(app_config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)

    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base = declarative_base()
    Base.query = db_session.query_property()

    Base.metadata.create_all(bind=engine)

    return
