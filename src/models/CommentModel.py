from src.utils.Logger import Logger
import traceback


class Comment:
    def __init__(self, id_user, comment, publication_date):
        self.id_user = id_user
        self.comment = comment
        self.publication_date = publication_date


class NewComment(Comment):
    def __init__(self, id_user, comment, publication_date, id_comment, id_post):
        super().__init__(id_user, comment, publication_date)
        self.id_comment = id_comment
        self.id_post = id_post
    
    def new_comment(self, connection):
        try:
            cursor = connection.cursor()

            insert_query = """
                INSERT INTO post_comments(id_comment, id_post, id_user, comment, publication_date)
                VALUES (%s, %s, %s, %s, %s)
            """
            data = (self.id_comment, self.id_post, self.id_user, self.comment, self.publication_date)
            cursor.execute(insert_query, data)

            connection.commit()

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()
    

class GetComments:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
        
    def get_comment(self, id_post):
        try:
            select_query = """
                SELECT post_comments.*, users.username, users.photo
                FROM post_comments
                JOIN users ON post_comments.id_user = users.id_user
                WHERE post_comments.id_post = 'bfb9656a-b321-4dfd-83cd-64e69dc0e614';
            """
            data = (id_post,)
            self.cursor.execute(select_query, data)

            data_comments = self.cursor.fetchall()

            return data_comments

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()
