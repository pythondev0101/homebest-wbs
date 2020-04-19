""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,\
    DateTimeField, SelectField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""


class BillCreateForm(FlaskForm):
    meter_no = StringField('Meter no', validators=[DataRequired()])
    customer_id = SelectField('Customer', validators=[DataRequired()])
    amount_due = DecimalField('Amount due',validators=[DataRequired()])
    period_from = DateField('Period From',validators=[DataRequired()])
    period_to = DateField('Period to',validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])

    active = BooleanField('Active',default=1)
    created_at = DateTimeField('Created At',format='%Y-%m-%dT%H:%M:%S', validators = [DataRequired()],
                               default=datetime.today())
