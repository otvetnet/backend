from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Application(BaseModel):
    name: str = "Untitled"


class Settings(BaseSettings):
    app: Application = Application()
    model_config = SettingsConfigDict(env_file=".env",
                                      env_nested_delimiter="__",
                                      env_file_encoding="utf-8")


@lru_cache()
def get_settings():
    return Settings()
