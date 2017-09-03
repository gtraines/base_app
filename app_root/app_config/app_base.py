from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore


class AppBase(object):

    def __init__(self, config):
        self.flask_app = self.create_app(config)
        self.flask_app.my_thing = self

    def __call__(self, environ, start_response):
        return self.flask_app(environ, start_response)

    @classmethod
    def create_app(self, config):
        app = Flask(__name__)
        # ex: dev database config, etc.
        app.config['DEBUG'] = True
        app.config['SECRET_KEY'] = 'super-secret'
        app.config['SECURITY_PASSWORD_SALT'] = 'super-secret'
        #init_db()
        user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
        security = Security(app, user_datastore)
        #security.init_app(app, user_datastore)
        #user_datastore.create_user(email='test_user1@nobien.net', username='test_user1@nobien.net', password='password')
        db_session.commit()
        app.config.update(config or {})
        # register_blueprints(app)
        # register_other_things(app)
        app.config.from_object(__name__)
        return app