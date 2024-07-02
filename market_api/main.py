from fastapi import FastAPI

from market_api.routers import info

app = FastAPI()

app.include_router(info)
