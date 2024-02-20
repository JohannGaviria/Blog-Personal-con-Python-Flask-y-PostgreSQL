from src.utils.Logger import Logger
import traceback


class Search:
    def __init__(self, query):
        self.query = query
    
    def seeker(self, connection):
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT id_user, name, username, photo, registration_date FROM users WHERE LOWER(username) LIKE LOWER(%s) OR LOWER(email) LIKE LOWER(%s)", (f"%{self.query}%", f"%{self.query}%"))
            users_data = cursor.fetchall()

            cursor.execute("SELECT COUNT(*) FROM users WHERE LOWER(username) LIKE LOWER(%s) OR LOWER(email) LIKE LOWER(%s)", (f"%{self.query}%", f"%{self.query}%"))
            users_count = cursor.fetchone()[0]

            cursor.execute("""
                SELECT posts.id_post, posts.title, posts.reading_time, users.id_user, users.username, users.photo, users.registration_date
                FROM posts
                JOIN users ON posts.id_user = users.id_user
                WHERE LOWER(title) LIKE LOWER(%s) OR LOWER(content) LIKE LOWER(%s)
            """, (f"%{self.query}%", f"%{self.query}%"))
            posts_data = cursor.fetchall()

            cursor.execute("SELECT COUNT(*) FROM posts WHERE LOWER(title) LIKE LOWER(%s) OR LOWER(content) LIKE LOWER(%s)", (f"%{self.query}%", f"%{self.query}%"))
            posts_count = cursor.fetchone()[0]

            return {
                'users_data': users_data,
                'users_count': users_count,
                'posts_data': posts_data,
                'posts_count': posts_count
            }

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()