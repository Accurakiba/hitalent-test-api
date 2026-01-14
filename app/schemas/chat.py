from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, field_validator

from app.schemas.message import MessageOut


class ChatCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)

    @field_validator("title")
    @classmethod
    def trim_title(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("title must not be empty")
        return v


class ChatOut(BaseModel):
    id: int
    title: str
    created_at: datetime

    model_config = {"from_attributes": True}


class ChatWithMessagesOut(ChatOut):
    messages: List[MessageOut]
