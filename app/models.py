from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .database import Base

class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class ItemSchema(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    class Config:
        orm_mode = True

