from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional

class ReceiptForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    items = TextAreaField('Items', validators=[DataRequired()])
    color = SelectField('Color', choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], validators=[Optional()])
    alignment = SelectField('Alignment', choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], validators=[Optional()])
    image = FileField('Image', validators=[Optional()])
