# FastAPI Translation Service

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск приложения

```bash
uvicorn main:app --reload
```

## Эндпоинт для перевода

- `POST /translate`
- Тело запроса (JSON):
  ```json
  {
    "text": "Текст для перевода",
    "dest": "kk"
  }
  ```
- Ответ:
  ```json
  {
    "translated": "Переведённый текст"
  }
  ```