from flask import Blueprint, render_template


main = Blueprint('home_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    return render_template('app/home.html', name_page="Inicio")