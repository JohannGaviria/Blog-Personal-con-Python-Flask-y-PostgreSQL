from flask import Blueprint, render_template, session, request, redirect, url_for


main = Blueprint('editProfile_blueprint', __name__)


@main.route('/profile')
def edit_profile():
    if 'id_user' in session:
        return render_template('app/edit-profile.html', name_page='Editar Perfil')
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))