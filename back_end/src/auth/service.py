from sqlmodel import select
from src.db.models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import (UserCreateModel,
                      UserLoginModel,
                      LoginResponseModel,
                      UserResponseModel,
                      TokenDetailsModel)
from .utils import get_hash_password, verify_password, create_access_token, create_refresh_token
from src.errors import UserAlreadyExists, InvalidCredentials, InvalidToken
from datetime import datetime

class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)
        res = await session.exec(statement=statement)
        user = res.first()
        return user

    async def user_exists(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email=email, session=session)
        return True if user else False

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):

        user_exists = await self.user_exists(email=user_data.email, session=session)

        if user_exists:
            raise UserAlreadyExists()

        user = user_data.model_dump()
        new_user = User(
            ** user
        )
        new_user.password = get_hash_password(user['password'])

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

    async def login(self, login_cred: UserLoginModel, session: AsyncSession):
        user = await self.get_user_by_email(login_cred.email, session)

        if not user:
            raise InvalidCredentials()
        
        if user.auth_provider != "local":
            raise InvalidCredentials()

        password_valid = verify_password(password=login_cred.password, hashed=user.password)

        if not password_valid:
            raise InvalidCredentials()
        
        access_token = create_access_token(
            user_data={
                "email": user.email,
                "user_uid": str(user.uid)
            }
        )

        refresh_token = create_refresh_token(
            user_data={
                "email": user.email,
                "user_uid": str(user.uid)
            }
        )

        return LoginResponseModel(
            message="Login Sucessfull!",
            access_token=access_token,
            refresh_token=refresh_token,
            user=UserResponseModel(email=user.email, uid=user.uid)
        )
    
    async def get_new_refresh_token(self, token: TokenDetailsModel, session: AsyncSession):
        if token.exp < datetime.now().timestamp():
            raise InvalidToken()
        
        return create_refresh_token(user_data=token.user_details)
            
    async def get_new_access_token(self, token:TokenDetailsModel, session: AsyncSession):
        if token.exp < datetime.now().timestamp():
            raise InvalidToken()
        
        return create_access_token(user_data=token.user_details)
    
    async def upsert_oauth_users(
            self,
            email: str,
            first_name: str,
            last_name: str,
            provider: str,
            session: AsyncSession
        ) -> User:
        user = await self.get_user_by_email(email=email,  session=session)

        if user:
            return user
        
        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=email.split("@")[0][:8],
            password="",
            auth_provider=provider,
            is_verified=True,
        )

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user