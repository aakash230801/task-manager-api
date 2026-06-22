from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserFacade:

    def __init__(self, db):
        self.repository = UserRepository(db)

    def create_user(self, payload):

        user = User(
            name=payload.name,
            email=payload.email,
            password=payload.password
        )

        return self.repository.create_user(user)