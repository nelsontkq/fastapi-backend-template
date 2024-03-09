from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.db import init_db
from api.routers import routers
from api.util.logging import init_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_logging()
    init_db()
    yield
    # on close


app = FastAPI(routers=routers, lifespan=lifespan)

[app.include_router(router) for router in routers]
