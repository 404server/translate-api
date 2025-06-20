# FastAPI Translation Service

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск приложения

```bash
uvicorn main:app --reload
```

## для многопоточки workers можно поменять 
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers  4                  
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