from functools import lru_cache

from pydantic import BaseModel, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Application(BaseModel):
    name: str = "Untitled"


class Database(BaseModel):
    scheme: str = "postgresql://"
    host: str = "db"
    user: str = "user"
    password: str = "pass"
    db_name: str = "db"
    port: int = 5432

    @computed_field
    def url(self) -> str:
        return (
            f"{self.scheme}{self.user}:{self.password}@"
            f"{self.host}:{self.port}/{self.db_name}"
        )


class OAuth2(BaseModel):
    secret_key: str = "secret"
    algorithm: str = "HS256"
    token_expire_minutes: int = 30


class Settings(BaseSettings):
    app: Application = Application()
    database: Database = Database()
    oauth2: OAuth2 = OAuth2()

    model_config = SettingsConfigDict(env_file=".env",
                                      env_nested_delimiter="__",
                                      env_file_encoding="utf-8")


@lru_cache()
def get_settings():
    return Settings()
