""" APP IMPORTS  """
from app import db
from app.core.models import Base,CoreProvince,CoreCity,CoreCustomer
from app.admin.models import Admin
"""--------------END--------------"""
from sqlalchemy.orm import column_property

class Bill(Base,Admin):
    __tablename__ = 'wbs_bill'
    meter_no = db.Column(db.Integer,nullable=False)
    customer_id = db.Column(db.Integer,db.ForeignKey('wbs_customer.id'))
    customer = db.relationship('Customer',cascade='all,delete',backref="bill")
    amount_due = db.Column(db.Numeric(10,2),nullable=False)
    period_from = db.Column(db.Date,nullable=False)
    period_to = db.Column(db.Date,nullable=False)
    due_date = db.Column(db.Date,nullable=False)

    model_name = 'Billing'
    model_icon = 'pe-7s-calculator'
    model_description = 'Billing'
    functions = {'View all': 'bp_wbs.index'}

    @property
    def name(self):
        return self.id

class Payment(Base,Admin):
    __tablename__ = 'wbs_payment'
    bill_id = db.Column(db.Integer,db.ForeignKey('wbs_bill.id'))
    bill = db.relationship('Bill',cascade='all,delete',backref="payment")
    customer_id = db.Column(db.Integer,db.ForeignKey('wbs_customer.id'))
    customer = db.relationship('Customer',cascade='all,delete',backref="payment")
    payment_date = db.Column(db.Date,nullable=False)
    amount_paid = db.Column(db.Numeric(10,2),nullable=False)
    payment_type_id = db.Column(db.Integer,db.ForeignKey('wbs_payment_type.id'))
    payment_type = db.relationship('PaymentType')

    model_name = 'Payment'
    model_icon = 'pe-7s-cash'
    model_description = 'Payments'
    functions = {'View all': 'bp_wbs.payment_index'}


class PaymentType(Base,Admin):
    __tablename__ = 'wbs_payment_type'
    name = db.Column(db.String(64),nullable=False)


class Customer(CoreCustomer,Admin):
    __tablename__ = 'wbs_customer'
    city_id = db.Column(db.Integer, db.ForeignKey('core_city.id'), nullable=True)
    city = db.relationship("CoreCity")
    province_id = db.Column(db.Integer, db.ForeignKey('core_province.id'), nullable=True)
    province = db.relationship("CoreProvince")
    
    @property
    def name(self):
        return self.fname + self.lname

    model_name = 'Customers'
    model_icon = 'pe-7s-users'
    model_description = 'Customers'
    functions = {'View all': 'bp_wbs.customer_index'}
