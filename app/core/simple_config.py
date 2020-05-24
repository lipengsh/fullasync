import secrets


class Settings():
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SERVER_NAME: str = "async"
    PROJECT_NAME = "full async"

    class Config:
        case_sensitive = True


settings = Settings()
