from flask import Blueprint
from app import system_modules

bp_wbs = Blueprint('bp_wbs', __name__,template_folder="templates")


from . import routes
from . import models


