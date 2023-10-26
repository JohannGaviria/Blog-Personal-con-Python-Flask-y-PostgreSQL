from flask import Blueprint, render_template


main = Blueprint('login_blueprint', __name__)


@main.route('/')
def login():
    return render_template('app/login.html')
