from typing import Callable, Type
from fastapi import Depends
from starlette.requests import Request
from ..repositories.base import BaseRepository
from ...db.db import get_session, AsyncSession


def get_repository(Repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(db: AsyncSession = Depends(get_session)) -> Type[BaseRepository]:
        return Repo_type(db)
    return get_repo
