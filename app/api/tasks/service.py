from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.tasks.repository import TaskRepository
from app.api.tasks.shemas import CreateTask, TaskInDb
from app.dependecies import get_session


def get_repository(session: AsyncSession = Depends(get_session)) -> TaskRepository:
    return TaskRepository(session)


class TaskService:
    def __init__(
        self,
        repository: TaskRepository = Depends(get_repository),
    ) -> None:
        self.repo = repository

    async def create(self, data: CreateTask) -> TaskInDb:
        return await self.repo.create(data)
    
    async def get_by_id(self, _id: int) -> TaskInDb:
        return await self.repo.get_by_id(_id)


    async def get_all(
        self, 
        offset: int = 0, 
        limit: int = 100
    ) -> list[TaskInDb] | None:
        return await self.repo.get_by_filters(offset, limit)
    
    async def delete_by_id(
        self,
        _id: int
    ) -> None:
        await self.repo.delete(_id)