from flask import Blueprint, render_template, session, redirect, url_for, request
from src.database.connection import connectionDB
from src.utils.Logger import Logger
from src.models.ProfileModel import Profile
import traceback


main = Blueprint('profile_blueprint', __name__)


def get_info_profile(username):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        profile = Profile(connection, cursor)
        info_profile = profile.get_info_profile(username)

        return info_profile

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


def get_info_post(id_user):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        profile = Profile(connection, cursor)
        info_post = profile.get_info_post(id_user)

        return info_post

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


def get_info_comment(id_user):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        profile = Profile(connection, cursor)
        info_comment = profile.get_info_comment(id_user)

        return info_comment

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


def get_info_quantity(id_user):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        profile = Profile(connection, cursor)
        info_quantity = profile.get_info_quantity(id_user)

        return info_quantity

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


@main.route('/<string:username>', methods=['GET'])
def profile(username):
    if 'id_user' in session:
        info_profile = get_info_profile(username)
        info_post = get_info_post(info_profile[0][0])
        info_comment = get_info_comment(info_profile[0][0])
        info_quantity = get_info_quantity(info_profile[0][0])
        
        return render_template('app/profile.html', name_page='Perfil', info_profile=info_profile, info_post=info_post, info_comment=info_comment, info_quantity=info_quantity)
    
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))