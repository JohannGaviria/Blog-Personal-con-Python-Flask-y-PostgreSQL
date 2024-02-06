from flask import Blueprint, redirect, url_for, session, request
from src.database.connection import connectionDB
from src.models.FollowModel import Follow
from src.utils.Logger import Logger
from datetime import datetime
import traceback
import uuid


main = Blueprint('follow_blueprint', __name__)


@main.route('/<int:id_following>')
def follow(id_following):
    if 'id_user' in session:
        id_follow = str(uuid.uuid4())
        id_follower = session['id_user']
        follow_date = datetime.now()

        try:
            connection = connectionDB()
            cursor = connection.cursor()

            follow = Follow(id_follow, id_follower, id_following, follow_date)
            follow.follow(connection)

            return redirect(url_for('home_blueprint.home'))

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()

    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))