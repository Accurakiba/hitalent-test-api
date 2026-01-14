from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.deps import get_db
from app.crud.chats import create_chat, get_chat, delete_chat
from app.crud.messages import create_message, get_last_messages
from app.schemas.chat import ChatCreate, ChatOut
from app.schemas.message import MessageCreate, MessageOut
from app.schemas.chat import ChatWithMessagesOut

router = APIRouter(prefix="/chats", tags=["chats"])


@router.post("/", response_model=ChatOut, status_code=status.HTTP_201_CREATED)
def create_chat_endpoint(payload: ChatCreate, db: Session = Depends(get_db)):
    title = payload.title.strip()
    return create_chat(db, title=title)


@router.post("/{chat_id}/messages/", response_model=MessageOut, status_code=status.HTTP_201_CREATED)
def send_message_endpoint(chat_id: int, payload: MessageCreate, db: Session = Depends(get_db)):
    chat = get_chat(db, chat_id)
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    text = payload.text.strip()
    return create_message(db, chat_id=chat_id, text=text)


@router.get("/{chat_id}", response_model=ChatWithMessagesOut)
def get_chat_with_messages_endpoint(
    chat_id: int,
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    chat = get_chat(db, chat_id)
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    messages = get_last_messages(db, chat_id=chat_id, limit=limit)
    return {"id": chat.id, "title": chat.title, "created_at": chat.created_at, "messages": messages}


@router.delete("/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chat_endpoint(chat_id: int, db: Session = Depends(get_db)):
    chat = get_chat(db, chat_id)
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    delete_chat(db, chat)
    return None
