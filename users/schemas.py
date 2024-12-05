from pydantic import BaseModel, EmailStr, constr
from annotated_types import MinLen, MaxLen
from typing import Annotated


class CreateUser(BaseModel):
    # username: Annotated[str, MinLen(3), MaxLen(20)]
    username: constr(min_length=5, max_length=10)
    email: EmailStr