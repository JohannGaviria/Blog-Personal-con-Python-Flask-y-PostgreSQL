from flask import Blueprint, render_template
from src.models.PostModel import GetPosts
from src.database.connection import connectionDB
from src.utils.Logger import Logger
from src.auth.MarkdownConvert import MarkdownConvert
import traceback


main = Blueprint('viewPost_blueprint', __name__)


@main.route('/<string:id_post>')
def view_post(id_post):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_posts = GetPosts(connection, cursor)
        post = get_posts.get_post_by_id(id_post)

        markdown_convert = MarkdownConvert(post[4])
        markdown_converted = markdown_convert.convert()

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

    finally:
        cursor.close()
        connection.close()

    return render_template('app/view-post.html', name_page="Vista Post", post=post, markdown_converted=markdown_converted)