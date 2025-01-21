# **Django backend for iot**

### Setup

Install packages

```
pip install -r requirements.txt
```

Apply migrations

```
cd iot_backend
python manage.py migrate
```

Start server

```
python manage.py runserver
```

Server will start at http://127.0.0.1:8000/

## Endpoints

### Users

GET, POST for users

http://127.0.0.1:8000/api/v1/users

GET, PATCH, DELETE for user

http://127.0.0.1:8000/api/v1/users/id

Examples:

GET response

```
[
    {
        "id": 2,
        "name": "t",
        "surname": "t",
        "rfid": "t",
        "created_at": "2025-01-21T14:10:09.511914Z",
        "updated_at": "2025-01-21T14:10:09.511981Z"
    },
    {
        "id": 3,
        "name": "Marcin",
        "surname": "Dolatowski changed",
        "rfid": "1234",
        "created_at": "2025-01-21T14:16:37.641006Z",
        "updated_at": "2025-01-21T15:30:02.136904Z"
    }
]
```

POST

```
{
    "name": "Marcin",
    "surname": "Dolatowski",
    "rfid": "12345"
}
```

GET user details

```
{
    "id": 3,
    "name": "Marcin",
    "surname": "Dolatowski changed",
    "rfid": "1234",
    "created_at": "2025-01-21T14:16:37.641006Z",
    "updated_at": "2025-01-21T15:30:02.136904Z"
}
```

PATCH

```
{
    "name": "Marcin imie changed"
}
```

## Questions

GET, POST for questions

http://127.0.0.1:8000/api/v1/questions

GET, PATCH, DELETE for question

http://127.0.0.1:8000/api/v1/questions/id

Examples:

GET response

```
[
    {
        "id": 1,
        "title": "default",
        "question": "Do you like bananas?",
        "created_at": "2025-01-21T14:16:45.990964Z",
        "updated_at": "2025-01-21T14:16:45.991043Z"
    },
    {
        "id": 2,
        "title": "glosowanie nr 2",
        "question": "chcemy przerwe?",
        "created_at": "2025-01-21T15:17:27.002465Z",
        "updated_at": "2025-01-21T15:17:27.002618Z"
    }
]
```

POST

```
{
    "title": "test",
    "question": "test"
}
```

GET question details response

```
{
    "id": 1,
    "title": "default",
    "question": "Do you like bananas?",
    "created_at": "2025-01-21T14:16:45.990964Z",
    "updated_at": "2025-01-21T14:16:45.991043Z"
}
```

PATCH

```
{
    "title": "Changed title"
}
```

## User Answers

GET, POST

http://127.0.0.1:8000/api/v1/user-answers/

GET response

```
[
  {
    "id": 1,
    "title": "default",
    "question": "Do you like bananas?",
    "za": 1,
    "przeciw": 2,
    "wstrzymal sie": 1
  },
  {
    "id": 2,
    "title": "glosowanie nr 2",
    "question": "chcemy przerwe?",
    "za": 1,
    "przeciw": 0,
    "wstrzymal sie": 0
  }
]
```

POST - answer have to be "za", "przeciw" or "wstrzymal sie"

```
{
    "user": 3,
    "question": 2,
    "answer": "za"
}
```
