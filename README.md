# Chat & Messages API  
- REST API для работы с чатами и сообщениями.

---

## Технологии  
- Python 3.12  
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- Alembic  
- Docker / Docker Compose

---

## Функциональность  
### Модели  
#### Chat  
- id: int  
- title: str  
- created_at: datetime

#### Message  
- id: int  
- chat_id: int  
- text: str  
- created_at: datetime

#### Связь: Chat 1 — N Message

---

## Запуск проекта
### 1. Поднять контейнеры
```bash
docker compose up --build -d
```

### 2. Применить миграции
```bash
docker compose exec api alembic upgrade head
```

### 3. Swagger UI
Открыть в браузере:
```bash 
http://localhost:8000/docs
```

---

## Тесты
- Тесты выполнены с помощью библиотеки `pytest`
- Выбранный для тестов эндпоинт проверен с использованием `httpx.AsyncClient`
- Выполнена проверка валидации pydentic-схемы для данного эндпоинта

### Запуск теста (локально)
```bash
pytest
```