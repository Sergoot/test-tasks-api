from pydantic import BaseModel


class BaseShema(BaseModel):

    class Config:
        orm_mode = True