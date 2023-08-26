from typing import TypeVar, Generic

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base_class import Base

_Model = TypeVar("_Model", bound=Base)


class MixinBase(Generic[_Model]):
    _session: AsyncSession
    _model: _Model
