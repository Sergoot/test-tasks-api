from fastapi import APIRouter, Depends, HTTPException, status

from app.api.users.service import UserService

from app.api.users.shemas import CreateUser, UserInDb

router =  APIRouter(prefix="/users", tags=["users, roles"])


@router.post("/", response_model=UserInDb)
async def create_user(
    body: CreateUser,
    service: UserService = Depends()
) -> UserInDb | None:
    user_in_db = await service.get_user_by_email(body.email)
    
    if user_in_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f"User with email {body.email} already exists"
        )
        
    return await service.create_user(body)