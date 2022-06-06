import os
from sqlmodel import SQLModel, create_engine, Session

from .config import DATABASE_URL
from ..models import *


engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    with Session(engine) as session:
        SQLModel.metadata.create_all(bind=engine)
