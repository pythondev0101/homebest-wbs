from flask import Blueprint
from app import system_modules,context

bp_admin = Blueprint('bp_admin',__name__,)

blueprint_name = "bp_admin"  # The name of the module's blueprint
module_name = "admin" # The name of the module

# URLS DICTIONARY
admin_urls = {
    'admin': 'bp_admin.index',
}

# TEMPLATES DICTIONARY
admin_templates = {
    'index': 'admin/admin_index.html',
}

# GLOBAL VARIABLE CONTEXT FOR URL RETURN
# context = {
#     'title': 'Admin',
#     'system_modules': system_modules,
#     'module': module_name,
#     'active': 'main_dashboard',
#     'forms': {},
# }
context['title'] = 'Admin'
context['module'] = 'admin'

from . import routes

