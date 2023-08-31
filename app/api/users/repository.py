
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.users.models import User
from app.api.users.shemas import CreateUser
from app.lib.base_repository import BaseRepo
from app.lib.mixins import (
    CreateMixin, 
    GetOnByFilterMixin,
    DeleteByIdMixin, 
    GetByIdMixin
)

class UserRepository(
    BaseRepo[User],
    CreateMixin[User, CreateUser],
    GetOnByFilterMixin[User]  
):
    def __init__(self, session: AsyncSession, model: User = User) -> None:
        super().__init__(session, model)