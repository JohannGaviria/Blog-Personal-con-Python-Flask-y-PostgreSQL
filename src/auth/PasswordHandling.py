import bcrypt

class PasswordSecurity:
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(hashed_password, input_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))
