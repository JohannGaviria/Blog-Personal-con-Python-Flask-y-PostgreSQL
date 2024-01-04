from flask import Blueprint, render_template
from src.database.connection import connectionDB
from src.utils.Logger import Logger
import traceback


main = Blueprint('relevantPosts_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def relevant_posts():
    try:
        connection = connectionDB()
        cursor = connection.cursor()

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()
    return render_template('app/home.html', name_page='Posts Relevantes')