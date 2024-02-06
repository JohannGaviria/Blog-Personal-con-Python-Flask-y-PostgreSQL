from src.utils.Logger import Logger
from src.auth.PasswordHandling import PasswordSecurity
from src.auth.UploadHandle import UploadHandler
from src.auth.PasswordHandling import PasswordSecurity
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
    
    def user_authentication(self, connection):
        try:
            cursor = connection.cursor()

            select_query = "SELECT * FROM users WHERE email = %s"
            data = (self.email,)

            cursor.execute(select_query, data)
            data_user = cursor.fetchone()

            if data_user:
                hash_password = data_user[5]

                password_security = PasswordSecurity()
                if password_security.verify_password(hash_password, self.password):
                    return {
                        'id_user': data_user[0],
                        'name': data_user[1],
                        'username': data_user[2],
                        'photo': data_user[3],
                        'email': data_user[4],
                        'bio': data_user[7],
                        'role': data_user[8]
                    }

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        
        finally:
            cursor.close()


class EditUser(User):
    def __init__(self, name, username, photo, email, password, bio):
        super().__init__(name, username, photo, email, password)
        self.bio = bio
    
    def edit_user_info(self, connection, id_user):
        try:
            cursor = connection.cursor()

            update_query = """
                UPDATE users
                SET name = %s, username = %s, email = %s, bio = %s
                WHERE id_user = %s
            """
            data = (self.name, self.username, self.email, self.bio, id_user)

            cursor.execute(update_query, data)

            connection.commit()

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()
    
    def edit_user_photo(self, connection, upload_folder, id_user):
        try:
            cursor = connection.cursor()

            upload_handler = UploadHandler(self.photo, upload_folder)
            uploaded_filename = upload_handler.save_image()

            update_query = """
                UPDATE users
                SET photo = %s
                WHERE id_user = %s
            """
            data = (uploaded_filename, id_user)

            cursor.execute(update_query, data)

            connection.commit()

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def edit_account_pass(connection, id_user, current_password, password):
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT password FROM users WHERE id_user = %s", (id_user,))
            data_password = cursor.fetchone()

            if data_password:
                stored_password = data_password[0]
                if PasswordSecurity.verify_password(stored_password, current_password):
                    hashed_password = PasswordSecurity.hash_password(password)
                    cursor.execute("UPDATE users SET password = %s WHERE id_user = %s", (hashed_password, id_user))
                    connection.commit()
            
            return None
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()

    
    @staticmethod
    def delete_account(connection, id_user):
        try:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM posts WHERE id_user = %s", (id_user,))
            cursor.execute("DELETE FROM post_comments WHERE id_user = %s", (id_user,))
            cursor.execute("DELETE FROM users WHERE id_user = %s", (id_user,))

            connection.commit()
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()

    
    @staticmethod
    def refresh_data(connection, id_user):
        try:
            cursor = connection.cursor()

            select_query = "SELECT * FROM users WHERE id_user = %s"
            data = (id_user,)

            cursor.execute(select_query, data)
            data_user = cursor.fetchone()

            return {
                'name': data_user[1],
                'username': data_user[2],
                'photo': data_user[3],
                'email': data_user[4],
                'bio': data_user[7]
            }

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()