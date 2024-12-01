from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from items_views import router as items_router


app = FastAPI()
app.include_router(items_router)

class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
def hello_index():
    return {
        'message': 'Hello index!'
    }


@app.get('/hello/')
def hello(name: str = "World"):
    name = name.strip().title()
    return {'message': f'Hello {name}!'}


@app.post('/users/')
def create_user(user: CreateUser):
    return {
        'message': 'success',
        'email': user.email,
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
