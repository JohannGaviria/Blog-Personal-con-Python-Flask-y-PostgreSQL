from src.utils.Logger import Logger
import traceback


class Follow:
    def __init__(self, id_follow, id_follower, id_following, follow_date):
        self.id_follow = id_follow
        self.id_follower = id_follower
        self.id_following = id_following
        self.follow_date = follow_date
    
    def follow(self, connection):
        try:
            cursor = connection.cursor()

            insert_query = "INSERT INTO followers (id_follow, id_follower, id_following, follow_date) VALUES (%s, %s, %s, %s)"
            data = (self.id_follow, self.id_follower, self.id_following, self.follow_date)

            cursor.execute(insert_query, data)
            connection.commit()

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def get_followers(connection, id_user):
        try:
            cursor = connection.cursor()

            select_query = """
                SELECT u.id_user, u.username, u.photo, f.*
                FROM public.users u
                JOIN public.followers f ON u.id_user = f.id_following
                WHERE f.id_follower = %s
                ORDER BY RANDOM() LIMIT 3;
            """

            data = (id_user,)

            cursor.execute(select_query, data)
            data_followers = cursor.fetchall()

            return data_followers

        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def suggest_followers(connection, id_user):
        try:
            cursor = connection.cursor()

            select_query = """
                WITH UserFollowings AS (
                    SELECT id_following
                    FROM followers
                    WHERE id_follower = %s
                )
                SELECT users.id_user, users.username, users.photo
                FROM users
                JOIN (
                    SELECT id_following
                    FROM followers
                    WHERE id_follower IN (SELECT id_following FROM UserFollowings)
                    UNION
                    SELECT id_follower
                    FROM followers
                    WHERE id_following IN (SELECT id_following FROM UserFollowings)
                ) AS ConnectedUsers ON users.id_user = ConnectedUsers.id_following
                WHERE users.id_user != %s
                AND users.id_user NOT IN (SELECT id_following FROM public.followers WHERE id_follower = %s)
                ORDER BY RANDOM() LIMIT 3
            """

            data = (id_user, id_user, id_user)

            cursor.execute(select_query, data)

            data_suggest = cursor.fetchall()

            return data_suggest

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()