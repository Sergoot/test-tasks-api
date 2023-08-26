
from sqlalchemy.ext.asyncio import AsyncSession

from app.lib.base_repository import BaseRepo
from app.api.tasks.models import Task
from app.api.tasks.shemas import CreateTask

from app.lib.mixins import (
    CreateMixin, 
    GetByFilterMixin, 
    DeleteByIdMixin, 
    GetByIdMixin
)


class TaskRepository(
    BaseRepo[Task],
    GetByIdMixin[Task],
    GetByFilterMixin[Task],
    CreateMixin[Task, CreateTask],
    DeleteByIdMixin[Task]
):
    def __init__(self, session: AsyncSession, model: Task = Task) -> None:
        super().__init__(session, model)

    