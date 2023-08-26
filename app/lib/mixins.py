from typing import Generic, Sequence, TypeVar

from sqlalchemy import ColumnExpressionArgument, select, delete
from fastapi.encoders import jsonable_encoder
from app.lib.base_mixin import MixinBase

from app.db.base_class import Base
from app.shemas import BaseShema


ModelType = TypeVar("ModelType", bound=Base)


class GetByFilterMixin(MixinBase[ModelType]):

    async def get_by_filters(
        self, 
        *filters: ColumnExpressionArgument[bool]
    ) -> Sequence[ModelType] | None:
        
        stmt = select(self._model).where(*filters)
        objs = await self._session.execute(stmt)
        return objs.all()
    

CreateShema = TypeVar("CreateShema", bound=BaseShema)


class CreateMixin(MixinBase[ModelType], Generic[ModelType, CreateShema]) :
    async def create(
        self, 
        create_data: CreateShema
    ) -> ModelType:
        
        obj_in_db = jsonable_encoder(create_data)
        db_obj = self._model(**obj_in_db)

        self._session.add(db_obj)
        await self._session.commit()
        await self._session.refresh(db_obj)

        return db_obj
    

class DeleteByIdMixin(MixinBase[ModelType]) :
    async def delete(self, _id: int) -> None:
        stmt = delete(self._model).where(self._model.id == _id)
        await self._session.execute(stmt)