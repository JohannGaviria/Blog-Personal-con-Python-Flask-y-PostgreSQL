from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from src.database.connection import connectionDB
from src.models.UserModel import LoginUser
from src.utils.Logger import Logger
import traceback
import re


main = Blueprint('login_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email:
            flash('El correo electrónico no puede estar vacío.','warning')
        elif re.search(r'[;\'"]', email):
            flash('El correo electrónico contiene caracteres no permitidos.', 'danger')

        if not password:
            flash('La contraseña no puede estar vacía.', 'warning')
        elif re.search(r'[;\'"]',password):
            flash('La contraseña contiene caracteres no permitidos.', 'danger')

        try:
            connection = connectionDB()
            login_user = LoginUser(email, password)
            data_user = login_user.user_authentication(connection)

            if data_user:
                session['id_user'] = data_user['id_user']
                session['name'] = data_user['name']
                session['username'] = data_user['username']
                session['photo'] = data_user['photo']
                session['role'] = data_user['role']

                flash(f"Bienvenido {session['username']}", 'success')
                return redirect(session.pop('redirect', url_for('home_blueprint.home')))
            else:
                flash('Usuario o Contraseña Incorrectos.', 'warning')
        
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
        
        finally:
            connection.close()
        
    return render_template('app/login.html', name_page="Inicio Sesion")
