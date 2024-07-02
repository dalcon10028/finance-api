from fastapi import FastAPI

from finance_api.routers import info

app = FastAPI()

app.include_router(info)
