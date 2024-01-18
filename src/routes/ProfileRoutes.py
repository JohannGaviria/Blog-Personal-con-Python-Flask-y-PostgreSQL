from flask import Blueprint, render_template, session, redirect, url_for, request


main = Blueprint('profile_blueprint', __name__)


@main.route('/')
def profile():
    if 'id_user' in session:
        return render_template('app/profile.html', name_page='Perfil')
    
    session['redirect'] = request.url
    return redirect(url_for('login_blueprint.login'))