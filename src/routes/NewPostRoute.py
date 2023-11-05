from flask import Blueprint, render_template


main = Blueprint('newPost_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def new_post():
    return render_template('app/new-post.html')