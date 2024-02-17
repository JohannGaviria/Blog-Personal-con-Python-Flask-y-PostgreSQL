from flask import Flask
from .routes import IndexRoutes, LoginRoutes, RegisterRoutes, HomeRoutes, NewPostRoutes, ViewPostRoutes, RecentPostsRoutes, RelevantPostsRoutes, NewCommentRoutes, ProfileRoutes, EditProfileRoutes, LogoutRoutes, EditAccountRoutes, DeleteAccountRoutes, FollowRoutes, LeaveFollowRoutes, AddFavoritesRoutes, DeleteFavoriteRoutes


app = Flask(__name__)


def init_app(config):
    app.config.from_object(config)

    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(HomeRoutes.main, url_prefix='/app/home')

    app.register_blueprint(ProfileRoutes.main, url_prefix='/app/profile')
    app.register_blueprint(EditProfileRoutes.main, url_prefix='/app/settings/profile')
    app.register_blueprint(EditAccountRoutes.main, url_prefix='/app/settings/account')
    app.register_blueprint(DeleteAccountRoutes.main, url_prefix='/app/settings/deleteAccount')

    app.register_blueprint(FollowRoutes.main, url_prefix='/app/follow')
    app.register_blueprint(LeaveFollowRoutes.main, url_prefix='/app/leaveFollow')

    app.register_blueprint(AddFavoritesRoutes.main, url_prefix='/app/addFavorite')
    app.register_blueprint(DeleteFavoriteRoutes.main, url_prefix='/app/deleteFavorite')

    app.register_blueprint(NewPostRoutes.main, url_prefix='/app/newPost')
    app.register_blueprint(ViewPostRoutes.main, url_prefix='/app/viewPost')
    app.register_blueprint(NewCommentRoutes.main, url_prefix='/app/viewPost')
    app.register_blueprint(RecentPostsRoutes.main, url_prefix='/app/recentPost')
    app.register_blueprint(RelevantPostsRoutes.main, url_prefix='/app/relevantPost')

    app.register_blueprint(RegisterRoutes.main, url_prefix='/app/auth/register')
    app.register_blueprint(LoginRoutes.main, url_prefix='/app/auth/login')
    app.register_blueprint(LogoutRoutes.main, url_prefix='/app/auth/logout')

    return app
