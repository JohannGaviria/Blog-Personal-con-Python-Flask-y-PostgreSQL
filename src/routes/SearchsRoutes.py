from flask import Blueprint, render_template, request, session, redirect, url_for
from src.database.connection import connectionDB
from src.models.SearchModel import Search
from src.models.FavoriteModel import Favorite
from src.models.FollowModel import Follow
from src.utils.Logger import Logger
import traceback


main = Blueprint('search_blueprint', __name__)


def get_searchs(query):
    try:
        connection = connectionDB()
        cursor = connection.cursor()

        search = Search(query)
        get_search = search.seeker(connection)

        return get_search

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


def check_verefy_following(id_following):
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

@main.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query', '')
    else:
        query = request.args.get('query', '')

    if not query:
        return redirect(url_for('home_blueprint.home'))

    get_search = get_searchs(query)

    id_posts = [post[0] for post in get_search['posts_data']]
    check_favorite_list = [check_verefy_favorite(id_post, session.get('id_user')) for id_post in id_posts]

    id_users = [user[0] for user in get_search['users_data']]
    check_following_list = [check_verefy_following(id_user) for id_user in id_users]

    data_search = {
        'posts_count': get_search['posts_count'],
        'users_count': get_search['users_count']
    }

    zipped_posts = zip(get_search['posts_data'], check_favorite_list)
    zipped_users = zip(get_search['users_data'], check_following_list)

    has_post = bool(get_search['posts_data'])
    has_user = bool(get_search['users_data'])

    return render_template('app/search.html', name_page='Busqueda', query=query, data_search=data_search, zipped_posts=zipped_posts, zipped_users=zipped_users, has_post=has_post, has_user=has_user)