from typing import List, Optional
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class PetResponse(BaseModel):
    id: int
    category: Optional[Category] = None
    name: str
    photoUrls: Optional[List[str]]
    tags: Optional[List[Tag]]
    status: str
