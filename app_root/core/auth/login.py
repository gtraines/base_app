from app_root.core.types.metasingleton import MetaSingleton
from flask_login import LoginManager


class LoginService(metaclass=MetaSingleton):
    _login_manager = None

    def init_app(self, app_instance):
        self._login_manager = LoginManager()
        self._login_manager.session_protection = 'strong'
        self._login_manager.login_view = 'auth.login'
        self._login_manager.init_app(app_instance)

        return self._login_manager

    def get_login_manager(self):
        return self._login_manager


