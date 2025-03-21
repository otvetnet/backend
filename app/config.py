from functools import lru_cache

from pydantic import BaseModel, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Application(BaseModel):
    name: str = "Untitled"

class Database(BaseModel):
    scheme: str = "postgresql://"
    user: str = "user"
    password: str = "password"
    db_name: str = "db_otvetnet"
    port: int = 5432
    docker_name: str = "db"

    @computed_field
    def url(self) -> str:
        return (
            f"{self.scheme}{self.user}:{self.password}@"
            f"{self.docker_name}:{self.port}/{self.db_name}"
        )

class Settings(BaseSettings):
    app: Application = Application()
    database: Database = Database()
    model_config = SettingsConfigDict(env_file=".env",
                                      env_nested_delimiter="__",
                                      env_file_encoding="utf-8")


@lru_cache()
def get_settings():
    return Settings()
