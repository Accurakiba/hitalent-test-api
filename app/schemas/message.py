from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class MessageCreate(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)

    @field_validator("text")
    @classmethod
    def trim_text(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("text must not be empty")
        return v


class MessageOut(BaseModel):
    id: int
    chat_id: int
    text: str
    created_at: datetime

    model_config = {"from_attributes": True}
