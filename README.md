# job-tracker-api

For venv run the below command in command prompt(terminal)
- venv\Scripts\activate.bat

To install the packages
- python -m pip install -r requirements.txt

To start the backend application
- python -m uvicorn app.main:app --reload

Without __init__.py, imports can become unreliable

job-tracker-api/
│
├── app/
│   │
│   ├── api/
│   │   └── routers/
│   │       ├── auth_router.py
│   │       ├── user_router.py
│   │       └── job_router.py
│   │
│   ├── facades/
│   │   ├── auth_facade.py
│   │   ├── user_facade.py
│   │   └── job_facade.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   └── job_repository.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── job.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── auth_schema.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   ├── utils/
│   │
│   └── main.py
│
├── tests/
│
├── alembic/
│
├── .env
├── requirements.txt
├── Dockerfile
└── README.md