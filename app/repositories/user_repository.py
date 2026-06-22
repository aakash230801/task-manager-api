class UserRepository:

    def __init__(self, db):
        self.db = db

    def create_user(self, user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user