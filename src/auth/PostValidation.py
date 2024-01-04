from src.models.PostModel import Posts
import re

class PostValidation(Posts):
    def __init__(self, cover_image, title, content):
        super().__init__(cover_image, title, content)
        self.errors = []
    
    def validation_data(self):
        if not self.title:
            self.errors.append({'message': 'El titulo no puede estar vacio.', 'category': 'warning'})
        elif not len(self.title) < 255:
            self.errors.append({'message': 'El titulo no puede tener mas de 255 caracteres', 'categeory': 'warning'})
        elif not re.match(r'^[a-zA-Z0-9\s\.,!?]*$', self.title):
            self.errors.append({'message': 'El título contiene caracteres no permitidos.', 'category': 'danger'})

    
    def has_errors(self):
        return bool(self.errors)

    def get_errors(self):
        return self.errors
