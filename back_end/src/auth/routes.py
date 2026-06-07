from fastapi import APIRouter, status, Depends
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import UserCreateModel, UserLoginModel, TokenDetailsModel
from .dependencies import get_user_service, RefreshTokenBearer, AccesTokenBearer
from .service import UserService

auth_router = APIRouter()

@auth_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def user_signup(user_data: UserCreateModel, 
                     session: AsyncSession = Depends(get_session),
                     user_service: UserService = Depends(get_user_service)):    
    return await user_service.create_user(user_data, session)

@auth_router.post('/login')
async def user_login(login_cred: UserLoginModel, 
                     session: AsyncSession = Depends(get_session),
                     user_service: UserService = Depends(get_user_service)):
    return await user_service.login(login_cred, session)

@auth_router.get('/refresh-token')
async def get_new_refresh_token(token: TokenDetailsModel = Depends(RefreshTokenBearer()), 
                            session: AsyncSession = Depends(get_session),
                            user_service: UserService = Depends(get_user_service)):
    return await user_service.get_new_refresh_token(token, session)

@auth_router.get('/access-token')
async def get_new_access_token(token: TokenDetailsModel = Depends(AccesTokenBearer()), 
                            session: AsyncSession = Depends(get_session),
                            user_service: UserService = Depends(get_user_service)):
    return await user_service.get_new_access_token(token, session)