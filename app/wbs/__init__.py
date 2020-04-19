from flask import Blueprint
from app import system_modules

bp_wbs = Blueprint('bp_wbs', __name__)

# URLS DICTIONARY
wbs_urls = {
    'index': 'bp_wbs.index',
}

# TEMPLATES DICTIONARY
wbs_templates = {
    'index': 'wbs/billing_index.html',
    'customer_index': 'wbs/customer_index.html'
}


from . import routes
from . import models


""" THIS IS FOR ADMIN MODELS """


class CustomerModel:
    model_name = 'Customers'
    model_icon = 'pe-7s-users'
    functions = {'View all': 'bp_wbs.customer_index'}


class BillingModel:
    model_name = 'Billing'
    model_icon = 'pe-7s-calculator'
    functions = {'View all': 'bp_wbs.index'}


class PaymentModel:
    model_name = 'Payment'
    model_icon = 'pe-7s-cash'
    functions = {'View users': 'bp_auth.index'}


class WBSModule:
    module_name = 'wbs'
    module_icon = 'fa-tint'
    module_link = 'bp_wbs.index'
    module_description = 'Water Billing'
    models = [BillingModel, CustomerModel, PaymentModel]

