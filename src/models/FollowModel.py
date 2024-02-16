#FOLLOWER -> SIGUE
#FOLLOWING -> SEGUIDO

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
    
    def get_follower_following(connection, id_user):
        try:
            cursor = connection.cursor()

            select_query = """
                SELECT
                    (SELECT COUNT(*) FROM followers WHERE id_following = %s),
                    (SELECT COUNT(*) FROM followers WHERE id_follower = %s)
            """
            data = (id_user, id_user)

            cursor.execute(select_query, data)

            info_follwer_following = cursor.fetchall()

            return info_follwer_following
        
        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('errot', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_followers(connection, id_user):
        try:
            cursor = connection.cursor()

            select_query = """
                SELECT users.id_user, users.username, users.photo, followers.*
                FROM users
                JOIN followers ON users.id_user = followers.id_following
                WHERE followers.id_follower = %s
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
    
    @staticmethod
    def check_verefy_following(connection, id_follower, id_following):
        try:
            cursor = connection.cursor()

            check_query = "SELECT COUNT(*) FROM followers WHERE id_follower = %s AND id_following = %s"
            check_data = (id_follower, id_following)

            cursor.execute(check_query, check_data)
            check_result = cursor.fetchone()

            if check_result[0] > 0:
                return True
            else:
                return False

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def leave_follower(connection, id_follower, id_following):
        try:
            cursor = connection.cursor()

            delete_query = "DELETE FROM followers WHERE id_follower = %s AND id_following = %s"
            data = (id_follower, id_following)

            cursor.execute(delete_query, data)

            connection.commit()
        
        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()