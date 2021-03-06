"""
  *@ClassName app
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 18:10
  *@Version 1.0
 """

from flask import Flask

# from app.models.user import db
from app.models.bases import db

def create_app():
    # app = Flask(__name__)
    app = Flask("app", static_folder="static", static_url_path="/image")    # http://127.0.0.1:5000/image/one.jpeg

    # app.config.from_object("app.config.secret")
    # app.config.from_object("app.config.setting")

    from app.config import secret
    from app.config import setting
    app.config.from_object(secret)
    app.config.from_object(setting)

    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


def register_blueprint(app: Flask):
    from app.auth import auth

    app.register_blueprint(auth)