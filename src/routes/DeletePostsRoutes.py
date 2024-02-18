from flask import Blueprint, redirect, url_for, request, session
from src.models.PostModel import Posts
from src.models.CommentModel import Comment
from src.database.connection import connectionDB
from src.utils.Logger import Logger
import traceback


main = Blueprint('deletePost_blueprint', __name__)


@main.route('/<string:id_post>')
def delete_post(id_post):
    if 'id_user' in session:
        try:
            connection = connectionDB()
            cursor = connection.cursor()

            Posts.delete_post(connection, id_post)

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()
        
        return redirect(url_for('profile_blueprint.profile', username = session['username']))
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))