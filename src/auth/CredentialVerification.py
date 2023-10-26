from src.database.connection import connectionDB
from src.utils.Logger import Logger
import traceback


class CredentialVerification:
    @staticmethod
    def is_username_unique(username):
        connection = connectionDB()
        cursor = connection.cursor()
        try:
            select_query = "SELECT COUNT(*) FROM users WHERE username = %s"
            data = (username,)
            cursor.execute(select_query, data)
            result_username = cursor.fetchone()
            if result_username and result_username[0] > 0:
                return False
            else:
                return True
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        finally:
            cursor.close()
    

    @staticmethod
    def is_email_unique(email):
        connection = connectionDB()
        cursor = connection.cursor()
        try:
            select_query = "SELECT COUNT(*) FROM users WHERE email = %s"
            data = (email,)
            cursor.execute(select_query, data)
            result_username = cursor.fetchone()
            if result_username and result_username[0] > 0:
                return False
            else:
                return True
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        finally:
            cursor.close()