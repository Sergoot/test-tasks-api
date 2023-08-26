from typing import Generic, TypeVar

from app.db.base_class import Base

from sqlalchemy.ext.asyncio import AsyncSession

_Model = TypeVar("_Model", bound=Base)


class BaseRepo(Generic[_Model]):
    
    def __init__(self, session: AsyncSession, model: _Model) -> None:
        self._session = session
        self._model = model
