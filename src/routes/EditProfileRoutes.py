from flask import Blueprint, render_template, session, request, redirect, url_for
from src.models.UserModel import EditUser
from src.database.connection import connectionDB
from src.utils.Logger import Logger
from decouple import config
import traceback


main = Blueprint('editProfile_blueprint', __name__)

def edit_user_info(name, username, photo, email, password, bio):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        edit_user = EditUser(name, username, photo, email, password, bio)
        edit_user_info = edit_user.edit_user_info(connection, session['id_user'])

        return edit_user_info

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


def edit_user_photo(name, username, photo, email, password, bio):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        edit_user = EditUser(name, username, photo, email, password, bio)

        edit_user_photo = None

        if 'photo' in request.files and request.files['photo'].filename != '':
            edit_user_photo = edit_user.edit_user_photo(connection, config('UPLOAD_FOLDER_USER'), session['id_user'])
            
        return edit_user_photo

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


def refresh_data(id_user):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        data_user = EditUser.refresh_data(connection, id_user)

        return data_user

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


@main.route('/', methods=['GET', 'POST'])
def edit_profile():
    if 'id_user' in session:
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            photo = request.files['photo']
            email = request.form['email']
            bio = request.form['bio']
            password = None

            edit_user_info(name, username, photo, email, password, bio)
            edit_user_photo(name, username, photo, email, password, bio)
            
            data_user = refresh_data(session['id_user'])

            session['name'] = data_user['name']
            session['username'] = data_user['username']
            session['email'] = data_user['email']
            session['photo'] = data_user['photo']
            session['bio'] = data_user['bio']

        return render_template('app/edit-profile.html', name_page='Editar Perfil')
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))