from sqlalchemy.ext.asyncio import AsyncSession
from app.api.users.shemas import CreateUser, UserInDb
from app.dependecies import get_session
from fastapi import Depends
from app.api.users.repository import UserRepository


def get_repository(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)


class UserService:
    def __init__(
        self,
        repository: UserRepository = Depends(get_repository),
    ) -> None:
        self.repo = repository
        
    async def create_user(self, data: CreateUser) -> UserInDb:
        return await self.repo.create(data)
    
    async def get_user_by_email(self, email: str) -> UserInDb | None:
        return await self.repo.get_one_by_filter(
            self.repo._model.email==email
        )