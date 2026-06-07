from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_TOKEN_EXPIRY_MINUTES: int
    REFRESH_TOKEN_EXPIRY_DAYS: int
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str
    GOOGLE_SERVER_METADATA_URL: str
    FRONTEND_URL: str

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra = "ignore"
    )


Config = Settings()