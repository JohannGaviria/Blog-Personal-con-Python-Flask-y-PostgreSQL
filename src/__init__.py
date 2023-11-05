from flask import Flask
from .routes import IndexRoutes, LoginRoutes, RegisterRoutes, HomeRoutes, NewPostRoute


app = Flask(__name__)


def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(HomeRoutes.main, url_prefix='/app/home')
    app.register_blueprint(NewPostRoute.main, url_prefix='/app/newPost')
    app.register_blueprint(RegisterRoutes.main, url_prefix='/app/auth/register')
    app.register_blueprint(LoginRoutes.main, url_prefix='/app/auth/login')

    return app
