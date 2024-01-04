from flask import Flask
from .routes import IndexRoutes, LoginRoutes, RegisterRoutes, HomeRoutes, NewPostRoutes, ViewPostRoutes, RecentPostsRoutes, RelevantPostsRoutes


app = Flask(__name__)


def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(HomeRoutes.main, url_prefix='/app/home')
    app.register_blueprint(NewPostRoutes.main, url_prefix='/app/newPost')
    app.register_blueprint(ViewPostRoutes.main, url_prefix='/app/viewPost')
    app.register_blueprint(RecentPostsRoutes.main, url_prefix='/app/recentPost')
    app.register_blueprint(RelevantPostsRoutes.main, url_prefix='/app/relevantPost')
    app.register_blueprint(RegisterRoutes.main, url_prefix='/app/auth/register')
    app.register_blueprint(LoginRoutes.main, url_prefix='/app/auth/login')

    return app
