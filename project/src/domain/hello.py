# from typing import Optional
from pydantic import BaseModel


class Hello(BaseModel):
    environment: str
    py_version: str
    event: str
