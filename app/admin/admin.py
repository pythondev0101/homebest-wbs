""" THIS IS FOR ADMIN MODELS """

from app.auth.models import User,Role
from app.core.core import CoreModule

class AdminModule(CoreModule):
    module_name = 'admin'
    module_icon = 'fa-home'
    module_link = 'bp_admin.dashboard'
    module_short_description = 'Administrator'
    module_long_description = "Administrator Dashboard and pages"
    models = [User]
    no_admin_models = [Role]
    version = '1.0'