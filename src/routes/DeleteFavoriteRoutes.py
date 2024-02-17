from flask import Blueprint, render_template, redirect, url_for, session, request
from src.database.connection import connectionDB
from src.models.FavoriteModel import Favorite
from src.utils.Logger import Logger
import traceback
import uuid


main = Blueprint('deleteFavorite_blueprint', __name__)


@main.route('/<string:id_post>')
def delete_favorite(id_post):
    if 'id_user' in session:
        id_favorite = str(uuid.uuid4())
        id_user = session['id_user']

        try:
            connection = connectionDB()
            cursor = connection.cursor()

            add_favorite = Favorite(id_favorite, id_post, id_user)
            add_favorite.delete_favorite(connection)

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()
        
        return redirect(url_for('home_blueprint.home'))

    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))