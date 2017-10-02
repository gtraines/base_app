# -*- coding: utf-8 -*-

from flask_security import SQLAlchemySessionUserDatastore


class AuthDatastore(SQLAlchemySessionUserDatastore):
    