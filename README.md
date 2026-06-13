# task-manager-api

For venv run the below command in command prompt(terminal)
- venv\Scripts\activate.bat

To install the packages
- pip install -r requirements.txt


task-manager-api/

├── app/
│
│── api/
│   └── v1/
│       ├── routers/
│       │   ├── auth_router.py
│       │   ├── user_router.py
│       │   └── task_router.py
│       │
│       └── router.py
│
│── core/
│   ├── config.py
│   ├── security.py
│   ├── exceptions.py
│   └── logger.py
│
│── db/
│   ├── database.py
│   └── session.py
│
│── models/
│   ├── user.py
│   └── task.py
│
│── schemas/
│   ├── auth.py
│   ├── user.py
│   └── task.py
│
│── repositories/
│   ├── user_repository.py
│   └── task_repository.py
│
│── facades/
│   ├── auth_facade.py
│   ├── user_facade.py
│   └── task_facade.py
│
│── services/
│   ├── jwt_service.py
│   ├── password_service.py
│   └── email_service.py
│
│── dependencies/
│   ├── auth_dependency.py
│   └── database_dependency.py
│
│── constants/
│   └── enums.py
│
│── utils/
│   └── helper.py
│
│── main.py
│
├── tests/
│
├── alembic/
│
├── .env
├── requirements.txt
└── README.md