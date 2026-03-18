from models import User
from utils import db_session
class UserRepository:
    def get_users(self):
        return db_session.query(User).all()
