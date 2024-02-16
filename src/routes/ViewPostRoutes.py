from flask import Blueprint, render_template
from src.models.PostModel import GetPosts
from src.models.CommentModel import GetComments
from src.database.connection import connectionDB
from src.utils.Logger import Logger
from src.auth.MarkdownConvert import MarkdownConvert
import traceback

main = Blueprint('viewPost_blueprint', __name__)

def get_post_details(id_post):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_posts = GetPosts(connection, cursor)
        post = get_posts.get_post_by_id(id_post)

        markdown_convert = MarkdownConvert(post[7])
        markdown_converted = markdown_convert.convert()

        return post, markdown_converted

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return None, None

    finally:
        cursor.close()
        connection.close()

def get_post_comments(id_post):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_comment = GetComments(connection, cursor)
        comments = get_comment.get_comment(id_post)

        return comments

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return None

    finally:
        cursor.close()
        connection.close()

def get_comment_count(id_post):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        get_comment = GetComments(connection, cursor)
        comment_count = get_comment.get_comment_count(id_post)

        return comment_count[0] if comment_count else 0

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return 0

    finally:
        cursor.close()
        connection.close()


@main.route('/<string:id_post>', methods=['GET', 'POST'])
def view_post(id_post):
    post, markdown_converted = get_post_details(id_post)
    comments = get_post_comments(id_post)
    comment_count = get_comment_count(id_post)

    return render_template('app/view-post.html', name_page="Vista Post", post=post, markdown_converted=markdown_converted, comments=comments, comment_count=comment_count)
