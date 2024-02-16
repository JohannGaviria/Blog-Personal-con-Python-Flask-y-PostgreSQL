from flask import Blueprint, render_template, session, url_for, request, redirect
from src.database.connection import connectionDB
from src.models.FollowModel import Follow
from src.utils.Logger import Logger
import traceback


main = Blueprint('leaveFollow_blueprint', __name__)


@main.route('/<int:id_following>')
def leave_follow(id_following):
    if 'id_user' in session:
        id_follower = session['id_user']

        try:
            connection = connectionDB()
            cursor = connection.cursor()

            Follow.leave_follower(connection, id_follower, id_following)
        
        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
        
        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('home_blueprint.home'))

    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))