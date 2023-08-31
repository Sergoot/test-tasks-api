from pydantic import EmailStr


from app.shemas import BaseShema


class CreateUser(BaseShema):
    email: EmailStr
    
    
        
    first_name: str | None = None
    second_name: str | None = None
    last_name: str | None = None
    
    password: str
    
    role_id: int




class UserInDb(CreateUser):
    id: int