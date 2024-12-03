from pydantic import BaseModel, EmailStr
from annotated_types import MinLen, MaxLen
from typing import Annotated


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr