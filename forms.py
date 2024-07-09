#forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional

class ReceiptForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    items = TextAreaField('Items', validators=[DataRequired()])
    color = SelectField('Color', choices=[('', 'Select Color'), ('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], validators=[Optional()])
    alignment = SelectField('Alignment', choices=[('', 'Select Alignment'), ('left', 'Left'), ('center', 'Center'), ('right', 'Right')], validators=[Optional()])
