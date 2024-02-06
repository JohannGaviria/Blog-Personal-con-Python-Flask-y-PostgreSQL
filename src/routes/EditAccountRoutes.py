from flask import Blueprint, render_template, redirect, url_for, request, session
from src.models.UserModel import EditUser
from src.database.connection import connectionDB
from src.utils.Logger import Logger
import traceback


main = Blueprint('editAccount_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def edit_account():
    if 'id_user' in session:
        if request.method == 'POST':
            current_password = request.form['current-password']
            password = request.form['password']
            new_password = request.form['new-password']

            try:
                connection = connectionDB()
                cursor = connection.cursor()
                
                if password == new_password:
                    EditUser.edit_account_pass(connection, session['id_user'], current_password, password, new_password)

                    session.pop('id_user', None)
                    return redirect(url_for('login_blueprint.login'))

            except Exception as ex:
                Logger.add_to_log("error", str(ex))
                Logger.add_to_log("error", traceback.format_exc())

            finally:
                cursor.close()
                connection.close()

        return render_template('app/edit-account.html', name_page='Editar Cuenta')
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))