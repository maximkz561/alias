from functools import lru_cache

from pydantic import BaseSettings


class Telegram(BaseSettings):
    api_id: str = ''
    api_hash: str = ''
    token: str = ''

    class Config:
        env_prefix = "TELEGRAM_"


class Settings(BaseSettings):
    telegram: Telegram = Telegram()


@lru_cache()
def get_config():
    return Settings()

