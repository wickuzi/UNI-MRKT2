from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, correo, password):
        self.id = id
        self.username = username
        self.correo = correo
        self.password = password

    @staticmethod
    def check_password(hash_from_db, password_input):
        return check_password_hash(hash_from_db, password_input)