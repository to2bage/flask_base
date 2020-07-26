"""
  *@ClassName user
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 18:23
  *@Version 1.0
 """

from flask import Blueprint, request, render_template
from app.utils.redprint import RedPrint

# from app.models.user import db
from app.models.bases import db
from app.models.user import User
from app.forms.user import UserForm

api = RedPrint("api")

print("name ", __name__)        #  app.auth.user
print("packag", __package__)    #  app.auth


@api.route("/index", methods=["POST"])
def index():
    nickname = request.form["nickname"]
    password = request.form["password"]

    user = User()
    user.nickname = nickname
    user.password = password        #  这里被加密了

    db.session.add(user)
    db.session.commit()

    return f"success user {nickname} and {password}"


@api.route("/create", methods=["POST"])
def create_user():
    form = UserForm(request.form)
    if form.validate():
        # user = User()
        # user.nickname = form.nickname.data
        # user.password = form.password.data
        #
        # db.session.add(user)
        # db.session.commit()

        with db.auto_commit():
            user = User()
            user.nickname = form.nickname.data
            user.password = form.password.data

            db.session.add(user)

        return f"success user {form.nickname.data} and {form.password.data}"
    else:
        return f"Failed {form.errors}"


@api.route("/h")
def halo():
    return render_template("index.html")