from flask import Blueprint, render_template, redirect, url_for, request, session


main = Blueprint('editAccount_blueprint', __name__)


@main.route('/account')
def edit_account():
    if 'id_user' in session:
        return render_template('app/edit-account.html', name_page='Editar Cuenta')
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))