# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AddressType(Base):
    __tablename__ = 'address_type'

    address_type_id = Column(Integer, primary_key=True, unique=True)
    address_type_uuid = Column(String(36), nullable=False, unique=True)
    slug = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(ForeignKey('user.user_id'), index=True)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(ForeignKey('user.user_id'), index=True)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user = relationship('User', primaryjoin='AddressType.created_by == User.user_id')
    user1 = relationship('User', primaryjoin='AddressType.deactivated_by == User.user_id')
    user2 = relationship('User', primaryjoin='AddressType.modified_by == User.user_id')


class ContactType(Base):
    __tablename__ = 'contact_type'

    contact_type_id = Column(Integer, primary_key=True, unique=True)
    contact_type_uuid = Column(String(36), nullable=False, unique=True)
    slug = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(ForeignKey('user.user_id'), index=True)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(ForeignKey('user.user_id'), index=True)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user = relationship('User', primaryjoin='ContactType.created_by == User.user_id')
    user1 = relationship('User', primaryjoin='ContactType.deactivated_by == User.user_id')
    user2 = relationship('User', primaryjoin='ContactType.modified_by == User.user_id')


class Metadatum(Base):
    __tablename__ = 'metadata'

    tablename_id = Column(Integer, primary_key=True, unique=True)
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(Integer, nullable=False)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)


class Organization(Base):
    __tablename__ = 'organization'

    organization_id = Column(Integer, primary_key=True, unique=True)
    organization_uuid = Column(String(36), nullable=False, unique=True)
    parent_organization_id = Column(String(36), index=True)
    organization_type_id = Column(ForeignKey('organization_type.organization_type_id'), nullable=False, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user = relationship('User')
    organization_type = relationship('OrganizationType')


class OrganizationAddres(Base):
    __tablename__ = 'organization_address'

    organization_address_id = Column(Integer, primary_key=True, unique=True)
    organization_address_uuid = Column(String(36), nullable=False, unique=True)
    organization_id = Column(ForeignKey('organization.organization_id'), nullable=False, index=True)
    address_type_id = Column(ForeignKey('address_type.address_type_id'), nullable=False, index=True)
    address_line_1 = Column(String(255), nullable=False, server_default=text("'1'"))
    address_line_2 = Column(String(255))
    city = Column(String(255), nullable=False)
    state_province = Column(String(128), nullable=False)
    country_id = Column(String(45))
    postal_code = Column(String(12), nullable=False)
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    address_type = relationship('AddressType')
    user = relationship('User')
    organization = relationship('Organization')


class OrganizationContact(Base):
    __tablename__ = 'organization_contact'

    organization_contact_id = Column(Integer, primary_key=True, unique=True)
    organization_contact_uuid = Column(String(36), nullable=False, unique=True)
    organization_id = Column(ForeignKey('organization.organization_id'), nullable=False, index=True)
    contact_type_id = Column(ForeignKey('contact_type.contact_type_id'), nullable=False, index=True)
    value = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    contact_type = relationship('ContactType')
    user = relationship('User')
    organization = relationship('Organization')


class OrganizationType(Base):
    __tablename__ = 'organization_type'

    organization_type_id = Column(Integer, primary_key=True, unique=True)
    organization_type_uuid = Column(String(36), nullable=False)
    slug = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user = relationship('User')


class OrganizationUserRole(Base):
    __tablename__ = 'organization_user_role'

    organization_user_role_id = Column(Integer, primary_key=True, unique=True)
    organization_user_role_uuid = Column(String(36), nullable=False, unique=True)
    organization_id = Column(ForeignKey('organization.organization_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    role_id = Column(ForeignKey('role.role_id'), nullable=False, index=True)
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user = relationship('User', primaryjoin='OrganizationUserRole.created_by == User.user_id')
    organization = relationship('Organization')
    role = relationship('Role')
    user1 = relationship('User', primaryjoin='OrganizationUserRole.user_id == User.user_id')


class Role(Base):
    __tablename__ = 'role'

    role_id = Column(Integer, primary_key=True, unique=True)
    role_uuid = Column(String(36), nullable=False, unique=True)
    parent_role_id = Column(ForeignKey('role.role_id'), index=True)
    role_type_id = Column(ForeignKey('role_type.role_type_id'), nullable=False, index=True)
    display_name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user = relationship('User')
    parent_role = relationship('Role', remote_side=[role_id])
    role_type = relationship('RoleType')


class RoleType(Base):
    __tablename__ = 'role_type'

    role_type_id = Column(Integer, primary_key=True, unique=True)
    role_type_uuid = Column(String(36), nullable=False, unique=True)
    organization_uuid = Column(Integer, nullable=False)
    slug = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(ForeignKey('user.user_id'), nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user = relationship('User')


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, unique=True)
    user_uuid = Column(String(36), nullable=False, unique=True)
    user_type_id = Column(ForeignKey('user_type.user_type_id'), nullable=False, index=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255))
    confirmed_at = Column(DateTime)
    current_login_at = Column(DateTime)
    current_login_ip = Column(String(45))
    last_login_at = Column(DateTime)
    last_login_ip = Column(String(45))
    login_count = Column(Integer, nullable=False, server_default=text("'0'"))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(Integer, nullable=False, index=True)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)

    user_type = relationship('UserType')


class UserType(Base):
    __tablename__ = 'user_type'

    user_type_id = Column(Integer, primary_key=True, unique=True)
    user_type_uuid = Column(String(36), nullable=False, unique=True)
    slug = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    display = Column(Integer, nullable=False, server_default=text("'1'"))
    created_date = Column(DateTime, nullable=False)
    created_by = Column(Integer, nullable=False)
    modified_date = Column(DateTime)
    modified_by = Column(Integer)
    deactivated_date = Column(DateTime)
    deactivated_by = Column(Integer)
    valid_from_date = Column(DateTime, nullable=False)
    valid_to_date = Column(DateTime)
