from fastapi import APIRouter

from app.api.tasks.router import router as task_router
from app.api.users.router import router as user_router


router = APIRouter()

router.include_router(task_router)
router.include_router(user_router)
