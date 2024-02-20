from flask import Blueprint, render_template, session
from src.utils.Logger import Logger
from src.database.connection import connectionDB
from src.models.PostModel import GetPosts
from src.models.FollowModel import Follow
from src.models.FavoriteModel import Favorite
import traceback


main = Blueprint('home_blueprint', __name__)


def get_post():
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_post = GetPosts(connection, cursor)
        get_posts = get_post.get_posts()

        return get_posts

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        
    finally:
        cursor.close()
        connection.close()


def get_follower():
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_followers = Follow.get_followers(connection, session.get('id_user'))

        return get_followers

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        
    finally:
        cursor.close()
        connection.close()


def get_suggest_follwer():
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_suggest_follwers = Follow.suggest_followers(connection, session.get('id_user'))

        return get_suggest_follwers

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


def check_verefy_favorite(id_post, id_user):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        check_verefy_favorite = Favorite.check_favorite(connection, id_post, id_user)

        return check_verefy_favorite

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()


@main.route('/', methods=['GET', 'POST'])
def home():
    get_posts = get_post()
    get_followers = get_follower()
    get_suggests = get_suggest_follwer()

    id_post = [id_post[0] for id_post in get_posts]
    check_favorite_list = []

    for id_post in id_post:
        check_favorite = check_verefy_favorite(id_post, session.get('id_user'))
        check_favorite_list.append(check_favorite)

    zipped_data = zip(get_posts, check_favorite_list)
    return render_template('app/home.html', zipped_data=zipped_data, get_followers=get_followers, get_suggests=get_suggests, name_page="Inicio")