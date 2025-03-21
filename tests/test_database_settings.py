import os

from pathlib import Path
import pytest
from pydantic_settings import SettingsConfigDict

from app.config import Settings, get_settings


@pytest.fixture(autouse=True)
def clear_settings_cache():
    get_settings.cache_clear()


def test_database_settings_default():
    env_path = Path(".env")
    if env_path.exists():
        os.rename(env_path, env_path.with_suffix(".env.bak"))

    try:
        settings = get_settings()
        db = settings.database
        assert db.user == "user"
        assert db.password == "password"
        assert db.db_name == "db_otvetnet"
        assert db.port == 5432
        assert db.docker_name == "db"
        assert db.url == "postgresql://user:password@db:5432/db_otvetnet"
    finally:
        if env_path.with_suffix(".env.bak").exists():
            os.rename(env_path.with_suffix(".env.bak"), env_path)


def test_database_settings_from_env(tmp_path):
    env_content = (
        "DATABASE__USER=\"testuser\"\n"
        "DATABASE__PASSWORD=\"testpass\"\n"
        "DATABASE__DB_NAME=\"testdb\"\n"
        "DATABASE__PORT=5433\n"
        "DATABASE__docker_name=\"testdb_service\""
    )
    env_file = tmp_path / ".env"
    env_file.write_text(env_content)

    class TestSettings(Settings):
        model_config = SettingsConfigDict(
            env_file=str(env_file),
            env_nested_delimiter="__",
            env_file_encoding="utf-8"
        )

    settings = TestSettings()
    db = settings.database
    assert db.user == "testuser"
    assert db.password == "testpass"
    assert db.db_name == "testdb"
    assert db.port == 5433
    assert db.docker_name == "testdb_service"
    assert db.url == "postgresql://testuser:testpass@testdb_service:5433/testdb"
