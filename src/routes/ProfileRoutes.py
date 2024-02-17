from flask import Blueprint, render_template, session, redirect, url_for, request
from src.database.connection import connectionDB
from src.utils.Logger import Logger
from src.models.ProfileModel import Profile
from src.models.FollowModel import Follow
from src.models.FavoriteModel import Favorite
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


def get_info_favorite():
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        favorite = Favorite.get_favorite(connection, session['id_user'])

        return favorite

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



def check_followings(id_following):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        check_verefy_following = Follow.check_verefy_following(connection, session['id_user'], id_following)

        return check_verefy_following

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
        info_favorite = get_info_favorite()
        info_quantity = get_info_quantity(info_profile[0][0])
        check_following = check_followings(info_profile[0][0])
        
        return render_template('app/profile.html', name_page='Perfil', info_profile=info_profile, info_post=info_post, info_comment=info_comment, info_favorite=info_favorite, info_quantity=info_quantity, check_following=check_following)
    
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))