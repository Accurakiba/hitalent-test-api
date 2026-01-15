import pytest
from httpx import ASGITransport, AsyncClient
from pydantic import ValidationError

from app.main import app
from app.schemas.chat import ChatOut


@pytest.mark.asyncio
async def test_post_chats(): # Тест ручки POST/chats/
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        r = await ac.post("/chats/", json={"title": "  New chat  "})
    
    assert r.status_code in (200, 201) # Проверка доступности ручки
    data = r.json()
    assert data["title"] == "New chat" # Проверка тримминга


@pytest.mark.asyncio
async def test_schema_compliance(): # Тест на соответствие pydentic-схеме
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        r2 = await ac.post("/chats/", json={"title": "  New chat  "})
    
    assert r2.status_code in (200, 201)
    data = r2.json()
    chat = ChatOut.model_validate(data) # Проверка на соответствие pydentic-схеме
