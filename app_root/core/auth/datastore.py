# -*- coding: utf-8 -*-

from flask_security import SQLAlchemySessionUserDatastore


class AuthDatastore(SQLAlchemySessionUserDatastore):

    def activate_user(self, user):
        return Super(user)