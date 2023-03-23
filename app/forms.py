from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo

class PhoneNumberForm(FlaskForm):
  first_name = StringField('First Name', validators=[InputRequired()])
  last_name = StringField('Last Name', validators=[InputRequired()])
  address = StringField('Address')
  phone_number = StringField('Phone Number', validators=[InputRequired()])
  confirm_phone_number = StringField('Confirm Phone Number', validators=[InputRequired(), EqualTo('phone_number')])
  submit = SubmitField('Register')

  