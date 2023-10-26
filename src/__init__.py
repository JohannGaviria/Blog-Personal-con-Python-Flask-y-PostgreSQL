from flask import Flask

# Routes
from .routes import IndexRoutes, LoginRoutes, RegisterRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(RegisterRoutes.main, url_prefix='/app/auth/register')
    app.register_blueprint(LoginRoutes.main, url_prefix='/app/auth/login')

    return app
