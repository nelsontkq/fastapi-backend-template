import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "WebApp"
    db_connection_string: str
    logging_level: int = logging.INFO
    model_config = SettingsConfigDict(env_file=".env")


app_settings = Settings()

