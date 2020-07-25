"""
  *@ClassName __init__.py
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 18:16
  *@Version 1.0
 """
from flask import Blueprint

from app.auth.user import api

auth = Blueprint("auth", __name__)
api.register_to(auth)