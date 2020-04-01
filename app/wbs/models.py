""" APP IMPORTS  """
from app import db
from app.core.models import Base,CoreProvince,CoreCity,CoreCustomer
"""--------------END--------------"""


class Bill(Base):
    __tablename__ = 'wbs_bill'
    meter_no = db.Column(db.Integer,nullable=False)
    customer_id = db.Column(db.Integer,db.ForeignKey('wbs_customer.id'))
    customer = db.relationship('Customer',cascade='all,delete',backref="bill")
    amount_due = db.Column(db.Float(9,2),nullable=False)
    period_from = db.Column(db.Date,nullable=False)
    period_to = db.Column(db.Date,nullable=False)
    due_date = db.Column(db.Date,nullable=False)


class Payment(Base):
    __tablename__ = 'wbs_payment'
    bill_id = db.Column(db.Integer,db.ForeignKey('wbs_bill.id'))
    bill = db.relationship('Bill',cascade='all,delete',backref="payment")
    customer_id = db.Column(db.Integer,db.ForeignKey('wbs_customer.id'))
    customer = db.relationship('Customer',cascade='all,delete',backref="payment")
    payment_date = db.Column(db.Date,nullable=False)
    amount_paid = db.Column(db.Float(9,2),nullable=False)
    payment_type_id = db.Column(db.Integer,db.ForeignKey('wbs_payment_type.id'))
    payment_type = db.relationship('PaymentType')


class PaymentType(Base):
    __tablename__ = 'wbs_payment_type'
    name = db.Column(db.String(64),nullable=False)


class Customer(CoreCustomer):
    __tablename__ = 'wbs_customer'
    city_id = db.Column(db.Integer, db.ForeignKey('wbs_city.id'), nullable=False)
    city = db.relationship("City")
    province_id = db.Column(db.Integer, db.ForeignKey('wbs_province.id'), nullable=False)
    province = db.relationship("Province")


class City(CoreCity):
    __tablename__ = 'wbs_city'


class Province(CoreProvince):
    __tablename__ = 'wbs_province'
