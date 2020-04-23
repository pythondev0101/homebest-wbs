from flask import Blueprint
from app import system_modules

bp_wbs = Blueprint('bp_wbs', __name__,template_folder="templates")

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


