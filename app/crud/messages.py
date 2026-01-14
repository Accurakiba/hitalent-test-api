from sqlalchemy.orm import Session
from sqlalchemy import select, desc

from app.models.message import Message


def create_message(db: Session, chat_id: int, text: str) -> Message:
    msg = Message(chat_id=chat_id, text=text)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def get_last_messages(db: Session, chat_id: int, limit: int) -> list[Message]:
    stmt = (
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(desc(Message.created_at))
        .limit(limit)
    )
    rows = db.execute(stmt).scalars().all()
    return list(reversed(rows))
