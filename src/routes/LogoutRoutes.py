from flask import Blueprint, redirect, url_for, session


main = Blueprint('logout_blueprint',__name__)


@main.route('/')
def logout():
    session.pop('id_user', None)
    return redirect(url_for('home_blueprint.home'))