from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings(BaseSettings):
    kis_prod_base_url: str
    kis_base_url: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


@lru_cache
def get_env():
    return EnvSettings()
