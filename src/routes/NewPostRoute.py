from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from src.auth.ReadingTime import ReadingTime
from src.models.PostModel import NewPost
from src.database.connection import connectionDB
from src.utils.Logger import Logger
from src.auth.PostValidation import PostValidation
from decouple import config
import datetime
import uuid
import traceback


main = Blueprint('newPost_blueprint', __name__)


@main.route('/', methods=['GET', 'POST'])
def new_post():
    if 'id_user' in session:
        if request.method == 'POST':
            id_post = str(uuid.uuid4())
            id_user = session['id_user']
            cover_image = request.files['image']
            title = request.form['title']
            content = request.form['content']
            publication_date = datetime.date.today().strftime("%d/%m/%Y")
            text = f"{title}\n{content}"
            reading_time = ReadingTime(text)
            reading_time = reading_time.calculate_reading_time()
            reading_time = f"{reading_time:.0f} min"

            post_validation = PostValidation(cover_image, title,content)
            post_validation.validation_data()
            
            if not post_validation.has_errors():
                try:
                    connection = connectionDB()

                    new_post = NewPost(cover_image, title, content, id_post, id_user, publication_date, reading_time)
                    new_post.upload_post(connection, config('UPLOAD_FOLDER_POST'))
                    flash('Publicacion subida exitosamente.', 'success')
                    return redirect(url_for('home_blueprint.home'))
                
                except Exception as ex:
                    Logger.add_to_log("error", str(ex))
                    Logger.add_to_log("error", traceback.format_exc())
                
                finally:
                    connection.close()
            else:
                for error in post_validation.get_errors():
                    flash(error['message'], error['category'])

        return render_template('app/new-post.html', name_page="Nuevo Post")
    return redirect(url_for('login_blueprint.login'))