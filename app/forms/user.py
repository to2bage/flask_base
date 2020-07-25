"""
  *@ClassName UserForm
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-25 19:03
  *@Version 1.0
 """

from wtforms import Form, StringField
from wtforms.validators import Length, DataRequired



class UserForm(Form):
    nickname = StringField(
        validators=[
            DataRequired(message=""),
            Length(min=5, max=30)
        ]
    )
    password = StringField(
        validators=[
            DataRequired(message=""),
            Length(min=5, max=100)
        ]
    )