from src.utils.Logger import Logger
import traceback


class Favorite:
    def __init__(self, id_favorite, id_post, id_user):
        self.id_favorite = id_favorite
        self.id_post = id_post
        self.id_user = id_user
    
    def add_favorite(self, connection):
        try:
            cursor = connection.cursor()

            insert_query = """
                INSERT INTO favorites(id_favorite, id_post, id_user)
                VALUES(%s, %s, %s)
            """

            data = (self.id_favorite, self.id_post, self.id_user)

            cursor.execute(insert_query, data)

            connection.commit()

        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_favorite(connection, id_user):
        try:
            cursor = connection.cursor()

            select_query = """
                SELECT users.id_user, users.photo, users.username, posts.id_post, posts.title, posts.publication_date, posts.reading_time, favorites.id_favorite
                FROM users
                JOIN favorites ON users.id_user = favorites.id_user
                JOIN posts ON favorites.id_post = posts.id_post
                WHERE users.id_user = %s;
            """
            data = (id_user,)

            cursor.execute(select_query, data)

            get_favorite = cursor.fetchall()

            return get_favorite

        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()

    def delete_favorite(self, connection):
        try:
            cursor = connection.cursor()

            delete_query = "DELETE FROM favorites WHERE id_post = %s AND id_user = %s"
            data = (self.id_post, self.id_user)

            cursor.execute(delete_query, data)

            connection.commit()

        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def check_favorite(connection, id_post, id_user):
        try:
            cursor = connection.cursor()

            check_query = "SELECT COUNT(*) FROM favorites WHERE id_post = %s AND id_user = %s"
            check_data = (id_post, id_user)

            cursor.execute(check_query, check_data)
            check_result = cursor.fetchone()

            if check_result[0] > 0:
                return True
            else:
                return False

        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()