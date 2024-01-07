from flask import Blueprint, redirect, url_for, session, request, flash
from src.models.CommentModel import NewComment
from src.database.connection import connectionDB
from src.utils.Logger import Logger
from datetime import datetime
import uuid
import traceback


main = Blueprint('newComment_blueprint', __name__)


@main.route('/<string:id_post>/comment', methods=['GET', 'POST'])
def new_comment(id_post):
    if request.method == 'POST':
        id_comment = str(uuid.uuid4())
        id_post = id_post
        id_user = session['id_user']
        comment = request.form['comment']
        publication_date = datetime.now().strftime('%d %b %Y')

        redirect_url = url_for('viewPost_blueprint.view_post', id_post=id_post)

        try:
            connection = connectionDB()
            cursor = connection.cursor()

            new_comment = NewComment(id_user, comment, publication_date, id_comment, id_post)
            new_comment.new_comment(connection)
            flash('Comentario subido exisotamente', 'succes')
            redirect_url = url_for('viewPost_blueprint.view_post', id_post=id_post)
            return redirect(redirect_url)

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()
    return redirect(redirect_url)