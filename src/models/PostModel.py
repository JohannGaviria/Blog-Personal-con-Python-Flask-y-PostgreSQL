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
