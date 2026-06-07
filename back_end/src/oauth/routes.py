from fastapi import APIRouter, Request, Depends
from .service import OAuthService
from .dependencies import get_oauth_service
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

oauth_router = APIRouter()


@oauth_router.get('/google')
async def google_login(request: Request,
                       oauth_service: OAuthService = Depends(get_oauth_service)):
    return await oauth_service.login(request)
    

@oauth_router.get('/google/callback')
async def google_callback(request: Request,
                          session: AsyncSession = Depends(get_session),
                          oauth_service: OAuthService = Depends(get_oauth_service)):
    return await oauth_service.create_access_token(request, session)