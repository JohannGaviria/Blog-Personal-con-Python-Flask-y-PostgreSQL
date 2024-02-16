from src.utils.Logger import Logger
import traceback


class Profile:
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
    
    def get_info_profile(self, username):
        try:
            select_query = """
                SELECT id_user, name, username, photo, registration_date, bio
                FROM users
                WHERE username = %s
            """
            data = (username,)

            self.cursor.execute(select_query, data)

            info_profile = self.cursor.fetchall()

            return info_profile

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()

    def get_info_post(self, id_user):
        try:
            select_query = """
                SELECT posts.id_post, posts.title, posts.publication_date, posts.reading_time, users.id_user, users.username, users.photo
                FROM posts
                JOIN users ON posts.id_user = users.id_user
                WHERE posts.id_user =  %s
                ORDER BY posts.publication_date DESC;
            """
            data = (id_user,)

            self.cursor.execute(select_query, data)

            info_post = self.cursor.fetchall()

            return info_post

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()
    
    def get_info_comment(self, id_user):
        try:
            select_query = """
                SELECT post_comments.*, posts.title
                FROM post_comments
                JOIN posts ON post_comments.id_post = posts.id_post
                WHERE post_comments.id_user =  %s
                ORDER BY post_comments.publication_date DESC;
            """
            data = (id_user,)

            self.cursor.execute(select_query, data)

            info_comment = self.cursor.fetchall()

            return info_comment

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()

    def get_info_quantity(self, id_user):
        try:
            select_query = """
                SELECT
                    followers_totals.total_followers,
                    followers_totals.total_following,
                    posts_totals.total_posts,
                    posts_totals.total_comments
                FROM
                    (SELECT
                        (SELECT COUNT(*) FROM public.followers WHERE id_following = %s) AS total_followers,
                        (SELECT COUNT(*) FROM public.followers WHERE id_follower = %s) AS total_following
                    ) AS followers_totals,
                    (SELECT
                        COUNT(DISTINCT posts.id_post) AS total_posts,
                        COUNT(DISTINCT post_comments.id_comment) AS total_comments
                    FROM
                        posts
                        LEFT JOIN post_comments ON post_comments.id_post = posts.id_post
                    WHERE
                        posts.id_user = %s
                    ) AS posts_totals;

            """
            data = (id_user, id_user, id_user)

            self.cursor.execute(select_query, data)

            info_quantity = self.cursor.fetchall()

            return info_quantity

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            self.cursor.close()
            self.connection.close()