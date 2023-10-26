from flask import Blueprint, render_template


main = Blueprint('index_blueprint', __name__)


@main.route('/')
def index():
    return render_template('index.html')
