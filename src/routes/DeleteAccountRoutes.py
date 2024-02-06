from flask import Blueprint, render_template, redirect, url_for, request, session
from src.models.UserModel import EditUser
from src.database.connection import connectionDB
from src.utils.Logger import Logger
import traceback


main = Blueprint('deleteAccount_blueprint', __name__)


@main.route('/')
def delete_account():
    if 'id_user' in session:
        try:
            connection = connectionDB()
            cursor = connection.cursor()

            EditUser.delete_account(connection, session['id_user'])
            session.pop('id_user', None)

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('home_blueprint.home'))
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))