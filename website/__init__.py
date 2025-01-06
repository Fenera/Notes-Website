from flask import Flask

def create_app():
    app = Flask(__name__) # initialize flask
    app.config['SECRET_KEY'] = "qwjd12o2j2nfj"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


