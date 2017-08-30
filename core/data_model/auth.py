from security.auth_db import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey

class RolesUsers(Base):
    __tablename__ = 'role_user'
    role_user_id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.user_id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.role_id'))

    def id(self):
        return self.role_user_id

class Role(Base, RoleMixin):
    __tablename__ = 'role'
    role_id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

    def id(self):
        return self.role_id

class User(Base, UserMixin):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='role_user', backref=backref('users', lazy='dynamic'))

    def id(self):
        return self.user_id