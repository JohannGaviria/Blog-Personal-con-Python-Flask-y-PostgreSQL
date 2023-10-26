from flask import Blueprint, render_template, request, flash, redirect, url_for
from src.database.connection import connectionDB
from src.models.UserModel import RegisterUser
from src.utils.Logger import Logger
from src.auth.CredentialValidation import CredentialValidation
from decouple import config
import datetime
import traceback


main = Blueprint('register_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        photo = request.files['photo']
        email = request.form['email']
        password = request.form['password']
        registration_date = datetime.date.today().strftime("%d/%m/%Y")

        credential_validation = CredentialValidation(name, username, photo, email, password)
        credential_validation.validator_data()

        if not credential_validation.has_errors():
            connection = connectionDB()
            cursor = connection.cursor()

            try:
                register_user = RegisterUser(name, username, photo, email, password, registration_date, bio="Ingrese su biografia...", role="user", status="inactive", last_login=None)
                register_user.register_to_db(connection, config('UPLOAD_FOLDER_USER'))
                flash('Registro completado exitosamente.', 'success')
                return redirect(url_for('login_blueprint.login'))

            except Exception as ex:
                Logger.add_to_log("error", str(ex))
                Logger.add_to_log("error", traceback.format_exc())

            finally:
                cursor.close()
                connection.close()
        else:
            for error in credential_validation.get_errors():
                flash(error['message'], error['category'])

    return render_template('app/register.html')
