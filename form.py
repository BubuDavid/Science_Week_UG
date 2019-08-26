from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class New_Member(Form):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    position = StringField('position', validators=[DataRequired()])
    social = StringField('social', validators=[DataRequired()])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    photo_link = StringField('photo_link', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
