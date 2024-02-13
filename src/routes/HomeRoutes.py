from flask import Blueprint, render_template, session
from src.utils.Logger import Logger
from src.database.connection import connectionDB
from src.models.PostModel import GetPosts
from src.models.FollowModel import Follow
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

        get_followers = Follow.get_followers(connection, session['id_user'])

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

        get_suggest_follwers = Follow.suggest_followers(connection, session['id_user'])

        return get_suggest_follwers

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

    return render_template('app/home.html', get_posts=get_posts, get_followers=get_followers, get_suggests=get_suggests, name_page="Inicio")