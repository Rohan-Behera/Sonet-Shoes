from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from .Config import Config

# API Routers
from src.auth.routes import auth_router
from src.orders.routes import orders_router
from src.shoes.routes import shoes_router
from src.oauth.routes import oauth_router


Version = "V1"
app = FastAPI(
    title="Sonet Shoes",
    description="A REST API for shoes website",
    version=Version
)

#Middleware config
app.add_middleware(SessionMiddleware, secret_key = Config.SECRET_KEY)

#API Routers
app.include_router(auth_router, prefix=f"/api/{Version}/auth", tags=["auth"])
app.include_router(oauth_router, prefix=f"/api/{Version}/oauth", tags=["oauth"])
app.include_router(orders_router, prefix=f"/api/{Version}/orders", tags=["orders"])
app.include_router(shoes_router, prefix=f"/api/{Version}/shoes", tags=["shoes"])
