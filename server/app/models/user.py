from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

from .organization_user_link import OrganizationUserLink
from .organization import *

class UserCredentials(SQLModel):
    login: str
    password: str

class UserAuthenticated(SQLModel):
    token: str
    expiration: datetime
    user_id: int

class UserBase(SQLModel):
    name: str
    login: str
    email: str
    is_active: Optional[bool] = True
    commission: Optional[float] = 5.0

class UserRead(UserBase):
    id: int

class UserReadInOrganization(SQLModel):
    id: int
    name: str
    is_active: bool
    permissions: str

class UserReadWithRelationships(UserRead):

    #m2m
    organizations: List['Organization'] = []

class UserCreate(UserBase):
    password: str

class UserValidation(UserCreate):
    id: int

class User(UserCreate, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    # Relationships

    #o2m
    events: List['Event'] = Relationship(back_populates='user')
    organizations_created: \
        Optional[List['Organization']] = Relationship(back_populates='created_by')



    organizations: List['Organization'] = Relationship(back_populates='users',
                                                       link_model=OrganizationUserLink)
    #m2m
    # organizations: List['OrganizationUserLink'] = Relationship(back_populates='user')


class UserCommission(SQLModel):
    id: int
    commission: float

class UserIsActive(SQLModel):
    id: int
    is_active: bool

