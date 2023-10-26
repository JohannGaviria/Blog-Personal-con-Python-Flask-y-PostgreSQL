from flask import flash
from src.auth.CredentialVerification import CredentialVerification
from src.models.UserModel import User
import re

class CredentialValidation(User):
    def __init__(self, name, username, photo, email, password):
        super().__init__(name, username, photo, email, password)
        self.errors = []

    def validator_data(self):
        if not self.name:
            self.errors.append({'message': 'El nombre no puede estar vacío.', 'category': 'warning'})
        elif re.search(r'[;\'"]', self.name):
            self.errors.append({'message': 'El nombre contiene caracteres no permitidos.', 'category': 'danger'})

        if not self.username:
            self.errors.append({'message': 'El nombre de usuario no puede estar vacío.', 'category': 'warning'})
        elif not 6 <= len(self.username) <= 16:
            self.errors.append({'message': 'El nombre de usuario debe tener entre 6 y 16 caracteres', 'category': 'warning'})
        elif not re.match("^[a-zA-Z0-9_]*$", self.username):
            self.errors.append({'message': 'El nombre de usuario no puede contener espacios ni caracteres especiales.', 'category': 'danger'})
        elif not CredentialVerification.is_username_unique(self.username):
            self.errors.append({'message': 'El nombre de usuario ya está en uso.', 'category': 'warning'})

        if not self.photo:
            self.errors.append({'message': 'Debe seleccionar una foto de perfil.', 'category': 'danger'})

        if not self.email:
            self.errors.append({'message': 'El correo electrónico no puede estar vacío.', 'category': 'warning'})
        elif re.search(r'[;\'"]', self.email):
            self.errors.append({'message': 'El correo electrónico contiene caracteres no permitidos.', 'category': 'danger'})
        elif not CredentialVerification.is_email_unique(self.email):
            self.errors.append({'message': 'El correo electrónico ya está en uso.', 'category': 'warning'})

        if not self.password:
            self.errors.append({'message': 'La contraseña no puede estar vacía.', 'category': 'warning'})
        elif len(self.password) < 8:
            self.errors.append({'message': 'La contraseña debe tener al menos 8 caracteres.', 'category': 'warning'})
        elif not any(char.isupper() for char in self.password):
            self.errors.append({'message': 'La contraseña debe contener al menos una letra mayúscula.', 'category': 'warning'})
        elif not any(char.isdigit() for char in self.password):
            self.errors.append({'message': 'La contraseña debe contener al menos un número.', 'category': 'warning'})
        elif re.search(r'[;\'"]', self.password):
            self.errors.append({'message': 'La contraseña contiene caracteres no permitidos.', 'category': 'danger'})

    def has_errors(self):
        return bool(self.errors)

    def get_errors(self):
        return self.errors
