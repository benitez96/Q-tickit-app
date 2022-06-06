from typing import Optional, TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship, Column, DateTime
from datetime import datetime

from .user import User
from .state import State


class EventCreate(SQLModel):
    name: str
    description: str
    start_date: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    end_date: datetime = Field(sa_column=Column(DateTime(timezone=True)))
    is_active: bool
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    #m2o
    user_id: int = Field(default=None, foreign_key='users.id')

    #TODO: quitar el optional
    organization_id: Optional[int] = Field(default=None, foreign_key='organization.id')


class Event(EventCreate, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)


    #m2o
    user: User = Relationship(back_populates='events')
    organization: 'Organization' = Relationship(back_populates='events')

    #o2m
    links: List['Link'] = Relationship(back_populates='event')

