from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from base_app import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

'''
import all modules here that might define models so that
they will be registered properly on the metadata.
Otherwise, you will have to import them first before calling
init_db()
'''
def init_db():
    from . import auth
    Base.metadata.create_all(bind=engine)
    return
