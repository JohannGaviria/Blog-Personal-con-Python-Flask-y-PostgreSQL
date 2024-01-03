from flask import Blueprint, render_template
from src.utils.Logger import Logger
from src.database.connection import connectionDB
from src.models.PostModel import GetPosts
import traceback


main = Blueprint('home_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_post = GetPosts(connection, cursor)
        get_posts = get_post.get_posts()

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        
    finally:
        cursor.close()
        connection.close()

    return render_template('app/home.html', get_posts=get_posts, name_page="Inicio")