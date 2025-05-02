from Models.Entities.User import User
from werkzeug.security import generate_password_hash, check_password_hash

class ModelUser:

    @classmethod
    def register(cls, db, user):
        try:
            cursor = db.connection.cursor()
            sql_check = "SELECT id FROM user WHERE correo = %s"
            cursor.execute(sql_check, (user.correo,))
            if cursor.fetchone():
                return "Correo ya registrado"

            # Cifrar la contraseña antes de guardarla
            hashed_password = generate_password_hash(user.password)
            sql_insert = "INSERT INTO user (username, correo, password) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (user.username, user.correo, hashed_password))
            db.connection.commit()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"

    @classmethod
    def login(cls, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, correo, password FROM user WHERE correo = %s"
            cursor.execute(sql, (user.correo,))
            row = cursor.fetchone()

            if row is not None:
                hash_from_db = row[3]
                password_correcta = check_password_hash(hash_from_db, user.password)
                if password_correcta:
                    return User(row[0], row[1], row[2], None)
            return None
        except Exception as ex:
            raise Exception(f"Error al hacer login: {ex}")
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, correo FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row is not None:
                    return User(row[0], row[1], row[2], None)
            else:
                  return None
        except Exception as ex:
            raise Exception(f"Error al hacer login: {ex}")