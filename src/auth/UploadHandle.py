from flask import flash
from src.utils.Logger import Logger
from werkzeug.utils import secure_filename
import os
import string
import random
import traceback


class UploadHandler:
    def __init__(self, file, upload_folder):
        self.file = file
        self.upload_folder = upload_folder


    def generate_random_filename(self):
        random_name = ''.join(random.choices(string.digits, k=10))
        return random_name


    def is_image(self, filename):
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


    def save_image(self):
        try:
            if self.file.filename == '':
                flash("El archivo no tiene nombre.", "danger")
                return None

            if not self.is_image(self.file.filename):
                flash("El archivo no es una imagen válida.", "danger")
                return None

            random_filename = self.generate_random_filename()

            filename = secure_filename(random_filename + os.path.splitext(self.file.filename)[1])

            self.file.save(os.path.join(self.upload_folder, filename))

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

        return filename