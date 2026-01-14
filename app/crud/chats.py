from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.chat import Chat


def create_chat(db: Session, title: str) -> Chat:
    chat = Chat(title=title)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_chat(db: Session, chat_id: int) -> Chat | None:
    stmt = select(Chat).where(Chat.id == chat_id)
    return db.execute(stmt).scalar_one_or_none()


def delete_chat(db: Session, chat: Chat) -> None:
    db.delete(chat)
    db.commit()
