# FastAPI Translation Service

## Описание
Этот проект предоставляет API для перевода текста с китайского на казахский язык с помощью различных переводчиков.

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
    "translated": "Переведённый текст",
    "count": 2
  }
  ```