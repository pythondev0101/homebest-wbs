""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,\
    DateTimeField, SelectField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""
from app.admin.forms import AdminIndexForm,AdminCreateField,AdminSelectField
from .models import Customer

class BillCreateForm(FlaskForm,AdminIndexForm):
    meter_no = StringField('Meter no', validators=[DataRequired()])
    customer_id = SelectField('Customer', validators=[DataRequired()])
    amount_due = DecimalField('Amount due',validators=[DataRequired()])
    period_from = DateField('Period From',validators=[DataRequired()])
    period_to = DateField('Period to',validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])

    active = BooleanField('Active',default=1)
    created_at = DateTimeField('Created At',format='%Y-%m-%dT%H:%M:%S', validators = [DataRequired()],
                               default=datetime.today())
    

    i_meter_no = AdminCreateField('meter_no','Meter no.','text')
    i_customer_id = AdminSelectField('customer_id','Customer','select',Customer)
    i_amount_due = AdminCreateField('amount_due','Amount due','number')
    i_period_from = AdminCreateField('period_from','period from','date')
    i_period_to = AdminCreateField('period_to','period to','number')
    i_due_date = AdminCreateField('due date','due date','date')

    index_headers = ['Bill No.','Customer Name','meter no.','amount due','period from','period to']
    index_title = 'Billings'
    index_message = ''
    create_fields =[
        [i_meter_no,i_customer_id],
        [i_amount_due,i_due_date],
        [i_period_from,i_period_to]
    ]
    title = index_title
