from fastapi import Request
from src.db.main import Config
from authlib.integrations.starlette_client import OAuth
from src.auth.service import UserService
from src.auth.utils import create_refresh_token, create_access_token
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.responses import RedirectResponse

oauth = OAuth()
oauth.register(
    name="google",
    client_id=Config.GOOGLE_CLIENT_ID,
    client_secret=Config.GOOGLE_CLIENT_SECRET,
    server_metadata_url=Config.GOOGLE_SERVER_METADATA_URL,
    client_kwargs={"scope": "openid email profile"},
)


class OAuthService():
    async def login(self, request: Request):
        redirect_url = Config.GOOGLE_REDIRECT_URI
        return await oauth.google.authorize_redirect(request, redirect_url)
    
    async def authenticate_user(self, request: Request, session: AsyncSession):
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get('userinfo')

        service = UserService()
        user = await service.upsert_oauth_users(
            email=user_info["email"],
            first_name=user_info.get("given_name", ""),
            last_name=user_info.get("family_name", ""),
            provider="google",
            session=session,
        )
        
        access_token = create_access_token({"email": user.email, "user_uid": str(user.uid)})
        refresh_token = create_refresh_token({"email": user.email, "user_uid": str(user.uid)})

        return RedirectResponse(
            url=f"{Config.FRONTEND_URL}/auth/callback?access_token={access_token}&refresh_token={refresh_token}"
        )