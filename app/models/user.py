"""
  *@ClassName user
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 18:40
  *@Version 1.0
 """
from sqlalchemy import Column, String, Integer
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy

from app.models.bases import Base

# db = SQLAlchemy()


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(32), unique=True, nullable=False)
    _password = Column("password", String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plain_txt):
        self._password = generate_password_hash(plain_txt)
