from typing import Annotated
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

from core.config import settings
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router
from core.models import db_helper, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)



@app.get('/')
def hello_index():
    return {
        'message': 'Hello index!'
    }


@app.get('/hello/')
def hello(name: str = "World"):
    name = name.strip().title()
    return {'message': f'Hello {name}!'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
