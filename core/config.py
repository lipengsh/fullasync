import secrets


class Settings():
    API_STR: str = "/api"
    SERVER_NAME: str = "async"
    PROJECT_NAME = "full async"

    class Config:
        case_sensitive = True


settings = Settings()
