"""
  *@ClassName __init__.py
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 18:16
  *@Version 1.0
 """
from flask import Blueprint

from app.auth.user import api

print("__name__ ", __name__)    #  app.auth
print("__package__", __package__)   # app.auth

auth = Blueprint("auth", __package__, template_folder="templates")      #  __package__ == "app.auth"
api.register_to(auth)