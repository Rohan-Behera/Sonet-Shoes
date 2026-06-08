from passlib.context import CryptContext
from datetime import datetime, timedelta
from src.Config import Config
import jwt
import uuid
from jwt.exceptions import PyJWTError
from src.errors import InvalidToken
from .schemas import TokenDetailsModel
from pydantic import ValidationError

password_context = CryptContext(
    schemes=['bcrypt']
)

# hashing the password
def get_hash_password(password: str) -> str:
    return password_context.hash(password)

# verifying hashed password when user logs in
def verify_password(password: str, hashed: str) -> str:
    return password_context.verify(secret=password, hash=hashed)

# create access token
def create_access_token(user_data: dict, expiry: timedelta = None):
    expiry_delta = expiry if expiry is not None else timedelta(minutes=Config.JWT_TOKEN_EXPIRY_MINUTES)
    payload = TokenDetailsModel(
        user_details=user_data,
        exp=(datetime.now() + expiry_delta).timestamp(),
        type="access",
        refresh=False,
        jti=str(uuid.uuid4())
    )
    return jwt.encode(payload= payload.model_dump(), key=Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)

# create refresh token
def create_refresh_token(user_data: dict, expiry: timedelta = None) -> str:
    expiry_delta = expiry if expiry is not None else timedelta(days=Config.REFRESH_TOKEN_EXPIRY_DAYS)
    payload = TokenDetailsModel(
        user_details=user_data,
        exp=(datetime.now() + expiry_delta).timestamp(),
        type="refresh",
        refresh=True,
        jti=str(uuid.uuid4())
    )
    return jwt.encode(payload=payload.model_dump(), key=Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)

# decode token
def decode_token(token: str) -> TokenDetailsModel:
    try:
        payload = jwt.decode(jwt=token, key=Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
        return TokenDetailsModel.model_validate(payload)
    except (PyJWTError, ValidationError):
        raise InvalidToken()