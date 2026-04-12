from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class Pet(BaseModel):
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photoUrls: list[str]
    tags: Optional[list[Tag]] = None
    status: Optional[str] = None