from src.utils.Logger import Logger, traceback
from src.auth.UploadHandle import UploadHandler


class Posts:
    def __init__(self, cover_image, title, content):
        self.cover_image = cover_image
        self.title = title
        self.content = content


class NewPost(Posts):
    def __init__(self, cover_image, title, content, id_post, id_user, publication_date, reading_time):
        super().__init__(cover_image, title, content)
        self.id_post = id_post
        self.id_user = id_user
        self.publication_date = publication_date
        self.reading_time = reading_time
    
    def upload_post(self, connection, upload_folder):
        try:
            cursor = connection.cursor()

            upload_handler = UploadHandler(self.cover_image, upload_folder)
            uploaded_filename = upload_handler.save_image()

            insert_query = "INSERT INTO posts (id_post, id_user, cover_image, title, content, publication_date, reading_time) VALUES (%s,%s, %s, %s, %s, %s, %s)"
            data = (self.id_post, self.id_user, uploaded_filename, self.title, self.content, self.publication_date, self.reading_time)

            cursor.execute(insert_query, data)
            connection.commit()
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        
        finally:
            cursor.close()


class GetPosts:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
    
    def get_posts(self):
        try:
            select_query = """
                SELECT posts.*, users.id_user, users.name, users.username, users.photo, users.email, users.registration_date, users.bio
                FROM posts
                JOIN users ON posts.id_user = users.id_user
                ORDER BY posts.publication_date DESC, RANDOM();
            """
            self.cursor.execute(select_query)

            data_posts = self.cursor.fetchall()

            return data_posts

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            
        finally:
            self.cursor.close()
            self.connection.close()
    
    def get_post_by_id(self, id_post):
        try:
            select_query = "SELECT * FROM posts WHERE id_post = %s"
            data = (id_post,)

            self.cursor.execute(select_query, data)

            post = self.cursor.fetchone()

            return post

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()
    
    def get_recent_posts(self):
        try:
            select_query = """
                SELECT posts.*, users.id_user, users.name, users.username, users.photo, users.email, users.registration_date, users.bio
                FROM posts
                JOIN users ON posts.id_user = users.id_user
                ORDER BY posts.publication_date DESC;
            """
            self.cursor.execute(select_query)

            data_posts = self.cursor.fetchall()

            return data_posts

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()
    
    def get_relevant_posts(self):
        try:
            select_query = """
                SELECT posts.*, users.id_user, users.name, users.username, users.photo, users.email, users.registration_date, users.bio, 
                COUNT(post_comments.id_comment) AS number_comments
                FROM posts
                JOIN users ON posts.id_user = users.id_user
                LEFT JOIN post_comments ON posts.id_post = post_comments.id_post
                GROUP BY posts.id_post, users.id_user,  users.name, users.username, users.photo, users.email, users.registration_date, users.bio
                ORDER BY number_comments DESC, posts.publication_date DESC;
            """
            self.cursor.execute(select_query)

            data_posts = self.cursor.fetchall()

            return data_posts

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()
