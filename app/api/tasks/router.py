from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.tasks.service import TaskService
from .shemas import CreateTask, TaskInDb


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskInDb)
async def create_task(
    body: CreateTask, 
    service: TaskService = Depends()
) -> TaskInDb:
    return await service.create(body)


@router.get("/", response_model=list[TaskInDb])
async def get_tasks(
    offset: int = 0,
    limit: int = 100,
    service: TaskService = Depends()
) -> list[TaskInDb] | None:
    return await service.get_all(offset, limit)


@router.delete("/{_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    _id: int,
    service: TaskService = Depends()
) -> None:
    task_to_delete = await service.get_by_id(_id)
    if task_to_delete:
        return await service.delete_by_id(_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
    )
    