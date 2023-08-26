from app.shemas import BaseShema


class CreateTask(BaseShema):
    title: str
    description: str


class TaskInDb(CreateTask):
    id: int