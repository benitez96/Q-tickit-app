from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

class OrganizationUserLink(SQLModel, table=True):
    # id: int = Field(default=None, primary_key=True)

    organization_id: Optional[int] = Field(primary_key=True, default=None, foreign_key='organization.id')
    # organization: 'Organization' = Relationship(back_populates='users')

    user_id: Optional[int] = Field(primary_key=True, default=None, foreign_key='users.id')
    # user: 'User' = Relationship(back_populates='organizations')

    # permissions: Optional[str] = "['camera','home']"
