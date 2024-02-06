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