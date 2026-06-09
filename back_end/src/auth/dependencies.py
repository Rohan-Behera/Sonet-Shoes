from fastapi import Depends
from fastapi.security import HTTPBearer
from .utils import decode_token
from src.errors import AccessTokenRequired, RefreshTokenRequired, InvalidToken, UserNotFound
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import UserService
from .schemas import TokenDetailsModel

# DI
def get_user_service() -> UserService:
    return UserService()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request):
        cred = await super().__call__(request)
        token = cred.credentials

        token_data = decode_token(token=token)
        if not token_data:
            raise InvalidToken()
        
        self.verify_token_data(token_data=token_data)
        return token_data
        
    def verify_token_data(self, token_data: TokenDetailsModel):
        raise NotImplementedError("Please override this method in child classes")

class AccessTokenBearer(JWTBearer):
    def verify_token_data(self, token_data: TokenDetailsModel):
        if token_data and token_data.refresh:
            raise AccessTokenRequired()
        
class RefreshTokenBearer(JWTBearer):
    def verify_token_data(self, token_data: TokenDetailsModel):
        if token_data and not token_data.refresh:
            raise RefreshTokenRequired()

async def get_current_user(token_details: TokenDetailsModel = Depends(AccessTokenBearer()),
                           session: AsyncSession = Depends(get_session),
                           user_service: UserService = Depends(get_user_service)):
    user_email = token_details.user_details["email"]
    user = await user_service.get_user_by_email(email=user_email, session=session)
    if not user:
        raise UserNotFound()
    
    return user