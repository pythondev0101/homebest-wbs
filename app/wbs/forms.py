""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,\
    DateTimeField, SelectField, DateField, DecimalField,IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""
from app.admin.forms import AdminIndexForm,AdminCreateField,AdminSelectField
from .models import Customer,Bill, PaymentType
from app.core.models import CoreCity,CoreProvince
class BillCreateForm(FlaskForm,AdminIndexForm):
    meter_no = StringField('Meter no', validators=[DataRequired()])
    customer_id = IntegerField('Customer', validators=[DataRequired()])
    amount_due = DecimalField('Amount due',validators=[DataRequired()])
    period_from = DateField('Period From',validators=[DataRequired()])
    period_to = DateField('Period to',validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])

    active = BooleanField('Active',default=1)
    created_at = DateTimeField('Created At',format='%Y-%m-%dT%H:%M:%S', validators = [DataRequired()],
                               default=datetime.today())
    

    i_meter_no = AdminCreateField('meter_no','Meter no.','text')
    i_customer_id = AdminSelectField('customer_id','Customer',Customer)
    i_amount_due = AdminCreateField('amount_due','Amount due','numeric')
    i_period_from = AdminCreateField('period_from','period from','date')
    i_period_to = AdminCreateField('period_to','period to','date')
    i_due_date = AdminCreateField('due_date','due date','date')

    index_headers = ['Bill No.','Customer','meter no.','amount due','period from','period to']
    index_title = 'Billings'
    index_message = ''
    create_fields =[
        [i_meter_no,i_customer_id],
        [i_amount_due,i_due_date],
        [i_period_from,i_period_to]
    ]
    title = index_title


class CustomerCreateForm(FlaskForm, AdminIndexForm):
    fname = StringField('fname', validators=[DataRequired()])
    lname = StringField('lname', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    zip = IntegerField('zip', validators=[DataRequired()])
    street = StringField('street', validators=[DataRequired()])
    city_id = IntegerField('city_id', validators=[DataRequired()])
    province_id = IntegerField('province_id', validators=[DataRequired()])

    i_fname = AdminCreateField('fname','first name','text')
    i_lname = AdminCreateField('lname','Last name','text')
    i_phone = AdminCreateField('phone','Phone','text')
    i_email = AdminCreateField('email','email','text')
    i_zip = AdminCreateField('zip','Zip code','number')
    i_street = AdminCreateField('street','street','text')
    i_city_id = AdminSelectField('city_id','city',CoreCity)
    i_province_id = AdminSelectField('province_id','province', CoreProvince)

    index_headers = ['first name','last name','phone','email']
    index_title = 'Customers'
    index_message = ''
    create_fields =[
        [i_fname,i_lname],
        [i_phone,i_email,i_zip],
        [i_street,i_city_id,i_province_id]
    ]
    title = index_title


class PaymentCreateForm(FlaskForm,AdminIndexForm):
    bill_id = IntegerField(validators=[DataRequired()])
    customer_id = IntegerField(validators=[DataRequired()])
    payment_date = DateField(validators=[DataRequired()])
    amount_paid = DecimalField(validators=[DataRequired()])
    payment_type_id = IntegerField(validators=[DataRequired()])

    i_bill_id = AdminSelectField('bill_id','Bill No.',Bill)
    i_customer_id = AdminSelectField('customer_id','Customer',Customer)
    i_payment_date = AdminCreateField('payment_date','Payment Date','date')
    i_amount_paid = AdminCreateField('amount_paid','Amount Paid','numeric')
    i_payment_type_id = AdminSelectField('payment_type_id','Payment Type',PaymentType)

    index_headers = ['Bill No.','customer','date of payment','Amount paid']
    index_title = 'Payments'
    create_fields = [
        [i_bill_id,i_customer_id],
        [i_payment_date,i_amount_paid,i_payment_type_id]
    ]
    title =index_title
    index_message = ''