from typing import List
from sqlmodel import select

from .base import BaseRepository
from ...models.event import *


class EventRepository(BaseRepository):

    def create_event(self, *, new_event: EventCreate) -> Event:
        event = Event(**new_event.dict())

        self.db.add(event)

        self.db.commit()
        self.db.refresh(event)

        return event


