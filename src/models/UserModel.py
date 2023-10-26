from flask import flash
from src.utils.Logger import Logger
from src.auth.PasswordHandling import PasswordSecurity
from src.auth.UploadHandle import UploadHandler
import traceback


class User:
    def __init__(self, name, username, photo, email, password):
        self.name = name
        self.username = username
        self.photo = photo
        self.email = email
        self.password = password


class RegisterUser(User):
    def __init__(self, name, username, photo, email, password, registration_date, bio, role, status, last_login):
        super().__init__(name, username, photo, email, password)
        self.registration_date = registration_date
        self.bio = bio
        self.role = role
        self.status = status
        self.last_login = last_login

    def register_to_db(self, connection, upload_folder):
        try:
            cursor = connection.cursor()

            password_security = PasswordSecurity()
            hashed_password = password_security.hash_password(self.password)

            upload_handler = UploadHandler(self.photo, upload_folder)
            uploaded_filename = upload_handler.save_image()

            insert_query = "INSERT INTO users (name, username, photo, email, password, registration_date, bio, role, status, last_login) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (self.name, self.username, uploaded_filename, self.email, hashed_password, self.registration_date, self.bio, self.role, self.status, self.last_login)
            cursor.execute(insert_query, data)

            connection.commit()

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()


class LoginUser:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    