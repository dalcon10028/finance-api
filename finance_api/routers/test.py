from typing import Annotated

from fastapi import APIRouter, Depends

from finance_api.configs import get_env, EnvSettings
from finance_api.configs.env import EnvSettings

router = APIRouter(prefix="/api/v1/test", tags=["test"])


@router.get("/env")
async def get_env(env: Annotated[EnvSettings, Depends(get_env)]) -> EnvSettings:
    return env
