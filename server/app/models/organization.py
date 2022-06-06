from typing import Optional, TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship

from .organization_user_link import OrganizationUserLink

class OrganizationCreate(SQLModel):

    name: str
    created_by: int
    city: Optional[str] = None
    state: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    # logo: Optional[bytes] = None
    is_active: Optional[bool] = True
    website: Optional[str] = None


class OrganizationRead(OrganizationCreate):
    id: int

    if TYPE_CHECKING:
        from .user import UserReadInOrganization

    users: List['UserReadInOrganization'] = []


class Organization(OrganizationCreate, table=True):

    id: Optional[int] = Field(default=None, primary_key=True, index=True)

    if TYPE_CHECKING:
        from .user import User
    #o2m
    events: List['Event'] = Relationship(back_populates='organization')

    created_by: Field(default=None, foreign_key='users.id')
    created_by: 'User' = Relationship(back_populates='organizations_created')

    #m2m
    users: List['User'] = Relationship(back_populates='organizations',
                                       link_model=OrganizationUserLink)


    class Config:
        orm_mode = True
