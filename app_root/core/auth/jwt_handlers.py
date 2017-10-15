import datetime
from flask import current_app
from app_root.core.data_model import auth
from .encryption import EncryptionService


def set_jwt_handlers(jwt):
    """Define handlers to jwt.

    :jwt: flask_jwt.JWT object
    :returns: None

    """

    @jwt.authentication_handler
    def authenticate(username, password):
        user = auth.User.objects(username=username).first()

        if user and EncryptionService().is_correct_password(password, user.password):
            return user
        return None

    @jwt.error_handler
    def error_handler(error):
        return 'Auth Failed: {}'.format(error.description), 400

    @jwt.payload_handler
    def make_payload(user):
        return {
            'user_id': str(user.id),
            'exp': (datetime.datetime.utcnow() +
                    current_app.config['JWT_EXPIRATION_DELTA']).isoformat()
        }

    @jwt.user_handler
    def load_user(payload):
        return auth.User.objects(id=payload['user_id']).first()
