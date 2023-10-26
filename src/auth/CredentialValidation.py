from flask import flash
from src.auth.CredentialVerification import CredentialVerification
from src.models.UserModel import User
import re


class CredentialValidation(User):
    def __init__(self, name, username, photo, email, password):
        super().__init__(name, username, photo, email, password)
    
    def validator_data(self):
        if not self.name:
            flash('El nombre no puede estar vacio.', 'warning')
        elif re.search(r'[;\'"]', self.name):
            flash('El nombre contiene caracteres no permitidos.', 'danger')

        if not self.username:
            flash('El nombre de usuario no puede estar vacio.', 'warning')
        elif not 6 <= len(self.username) <= 16:
            flash('El nombre de usuario debe tener entre 6 y 16 caracteres', 'warning')
        elif re.search(r'[;\'"]', self.username):
            flash('El nombre de usuario contiene caracteres no permitidos.', 'danger')
        elif not CredentialVerification.is_username_unique(self.username):
            flash('El nombre de usuario ya esta en uso.', 'warning')
        
        if not self.photo:
            flash('Debe de selecionar una foto de perfil.', 'warning')

        if not self.email:
            flash('El correo electrónico no puede estar vacío.')
        elif re.search(r'[;\'"]', self.email):
            flash('El correo electrónico contiene caracteres no permitidos.')
        elif not CredentialVerification.is_email_unique(self.email):
            flash('El correo electronico ya esta en uso.', 'warning')

        if not self.password:
            flash('La contraseña no puede estar vacía.', 'warning')
        elif len(self.password) < 8:
            flash('La contraseña debe tener al menos 8 caracteres.', 'warning')
        elif not any(char.isupper() for char in self.password):
            flash('La contraseña debe contener al menos una letra mayúscula.', 'warning')
        elif not any(char.isdigit() for char in self.password):
            flash('La contraseña debe contener al menos un número.', 'warning')
        elif re.search(r'[;\'"]', self.password):
            flash('La contraseña contiene caracteres no permitidos.', 'danger')
