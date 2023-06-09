from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired


class DataSetForm(FlaskForm):
    value = DecimalField("New Value", validators=[DataRequired()])
    dropdown = SelectField("Choose Accuracy:",
                           choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                           validators=[DataRequired()], default=3)
    submit = SubmitField("Enter", validators=[])
