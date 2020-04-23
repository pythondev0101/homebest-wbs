""" THIS IS FOR ADMIN MODELS """
from .models import Bill,Customer,Payment

class WBSModule:
    module_name = 'wbs'
    module_icon = 'fa-tint'
    module_link = 'bp_wbs.index'
    module_description = 'Water Billing'
    models = [Bill, Customer, Payment]

