""" FLASK IMPORTS """
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,\
    DateTimeField, SelectField, DateField, DecimalField,IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from datetime import datetime
"""--------------END--------------"""
from app.admin.forms import AdminIndexForm, AdminEditForm,AdminField, AdminInlineForm
from .models import Customer,Bill, PaymentType
from app.core.models import CoreCity,CoreProvince


class BillForm():
    meter_no = AdminField(label='Meter no', validators=[DataRequired()])
    customer_id = AdminField(label='Customer', validators=[DataRequired()],model=Customer)
    previous_reading = AdminField(label='Previous Reading',validators=[DataRequired()],input_type='number')
    present_reading = AdminField(label="Present Reading",validators=[DataRequired()],input_type='number')
    amount_due = AdminField(label='Amount due',validators=[DataRequired()],input_type='numeric',placeholder="PHP")
    period_from = AdminField(label='Period From',required=False,input_type='date')
    period_to = AdminField(label='Period to',required=False,input_type='date')
    due_date = AdminField(label='Due Date', required=False,input_type='date')

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        if not self.due_date.data:
            self.due_date.data = None
        if not self.period_from.data:
            self.period_from.data = None
        if not self.period_to.data:
            self.period_to.data = None


class BillCreateForm(BillForm,AdminIndexForm):
    index_headers = ['Bill No.','Customer','meter no.','amount due','period from','period to']
    index_title = 'Billings'
    index_message = ''

    def create_fields(self):
        return [[self.meter_no,self.customer_id],[self.previous_reading,self.present_reading],[self.amount_due,self.due_date],[self.period_from,self.period_to]]



class BillEditForm(BillForm,AdminEditForm):
    def edit_fields(self):
        return [[self.meter_no,self.customer_id],[self.amount_due,self.due_date],[self.period_from,self.period_to]]

    edit_title = "Edit bill"
    edit_message = "message"


class BillingInlineForm(AdminInlineForm):
    headers = ['Bill No.','Meter No.','Previous Reading','Present Reading','Amount due']
    title = "Billings"
    html = 'wbs/billing_inline.html'

class PaymentInlineForm(AdminInlineForm):
    headers = ['Bill no.','Payment Date', 'Amount paid']
    title = 'Payments'
    html = 'wbs/payment_inline.html'


class CustomerForm():
    fname = AdminField(label='First name', validators=[DataRequired()],placeholder='Robert')
    lname = AdminField(label='lname', validators=[DataRequired()],placeholder='Montemayor')
    phone = AdminField(label='phone', required=False)
    email = AdminField(label='email', required=False)
    zip = AdminField(label='zip', required=False)
    street = AdminField(label='street', required=False)
    city_id = AdminField(label='city', required=False,model=CoreCity)
    province_id = AdminField(label='province', required=False,model=CoreProvince)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if not self.phone.data:
            self.phone.data = ''
        if not self.email.data:
            self.email.data = None
        if not self.zip.data:
            self.zip.data = None
        if not self.street.data:
            self.street.data = ''
        if not self.city_id.data:
            self.city_id.data = None
        if not self.province_id.data:
            self.province_id.data = None

class CustomerCreateForm(CustomerForm,AdminIndexForm):
    index_headers = ['first name','last name','phone','email']
    index_title = 'Customers'
    index_message = ''

    def create_fields(self):
        return [
            [self.fname,self.lname],
            [self.phone,self.email,self.zip],
            [self.street,self.city_id,self.province_id]
            ]


class CustomerEditForm(CustomerForm,AdminEditForm):
    def edit_fields(self):
        return [
            [self.fname,self.lname],
            [self.phone,self.email,self.zip],
            [self.street,self.city_id,self.province_id]
            ]

    edit_title = "Edit customer"
    edit_message = "message"
    
    billing_inline = BillingInlineForm()
    payment_inline = PaymentInlineForm()
    inlines = [billing_inline,payment_inline]


class PaymentForm():
    bill_id = AdminField(label='bill',validators=[DataRequired()],model=Bill)
    customer_id = AdminField(label='customer',validators=[DataRequired()],model=Customer)
    payment_date = AdminField(label='payment date',validators=[DataRequired()],input_type="date")
    amount_paid = AdminField(label='amount paid',validators=[DataRequired()],input_type='numeric')
    payment_type_id = AdminField(label='Payment type',model=PaymentType,required=False)


class PaymentCreateForm(PaymentForm,AdminIndexForm):
    index_headers = ['Bill No.','customer','date of payment','Amount paid']
    index_title = 'Payments'
    index_message = ''
    
    def create_fields(self):
        return [
            [self.bill_id,self.customer_id],
            [self.payment_date,self.amount_paid,self.payment_type_id]
        ]


class PaymentEditForm(PaymentForm,AdminEditForm):
    edit_title = "Edit payment"
    edit_message = ""

    def edit_fields(self):
        return [
            [self.bill_id,self.customer_id],
            [self.payment_date,self.amount_paid,self.payment_type_id]
        ]


class PaymentTypeCreateForm(AdminIndexForm):
    name = AdminField(label='name',validators=[DataRequired()])
    index_headers = ['Name','Created at']
    index_title = 'Payment Types'

    def create_fields(self):
        return [[self.name]]