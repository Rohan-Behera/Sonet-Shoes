from .service import OAuthService

def get_oauth_service() -> OAuthService:
    return OAuthService()