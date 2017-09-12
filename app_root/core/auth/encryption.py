from app_root.core.types.metasingleton import MetaSingleton
from flask_bcrypt import generate_password_hash
from flask_bcrypt import Bcrypt


class EncryptionService(metaclass=MetaSingleton):
    _bcrypt_instance = None

    def init_app(self, app_instance):
        self._bcrypt_instance = Bcrypt(app_instance)
        return self._bcrypt_instance

    def generate_password_hash(self, plaintext):
        if self._bcrypt_instance is None:
            return generate_password_hash(plaintext, 24)

        return self._bcrypt_instance.generate_password_hash(plaintext)
