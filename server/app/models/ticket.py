from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

#%% Tickets


class Ticket(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    customer: str
    customer_dni: str
    customer_email: str
    customer_phone: str
    customer_address: str


    state_id: int = Field(default=None, foreign_key='state.id')
    state: 'State' = Relationship(back_populates='tickets')

    link_id: int = Field(default=None, foreign_key='link.id')
    ticket_link: 'Link' = Relationship(back_populates='tickets')
