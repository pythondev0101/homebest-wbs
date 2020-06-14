""" THIS IS FOR ADMIN MODELS """
from .models import Bill,Customer,Payment,PaymentType
from app.core.core import CoreModule
class WBSModule(CoreModule):
    module_name = 'wbs'
    module_icon = 'fa-tint'
    module_link = 'bp_wbs.index'
    module_short_description = 'Water Billing'
    module_long_description = 'Manage customer water bills'
    models = [Bill, Customer, Payment]
    version = '1.0'
    no_admin_models = [PaymentType]
