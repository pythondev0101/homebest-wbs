from flask import Blueprint
from app import system_models

bp_wbs = Blueprint('bp_wbs', __name__)

# URLS DICTIONARY
wbs_urls = {
    'index': 'bp_wbs.index',
}

context = {
    'title': 'Users',
    'system_models': system_models,
    'active': 'Users',
    'forms': {},
    'modal': False,
}

from . import routes
from . import models


