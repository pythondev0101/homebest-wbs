from app.wbs import bp_wbs
from .models import Customer
from flask_login import login_required
from flask import render_template
from . import wbs_templates,wbs_urls
from app import system_models,system_modules


# GLOBAL VARIABLE CONTEXT FOR URL RETURN
context = {
    'title': 'Water Billing',
    'system_models': system_models,
    'modules': system_modules,
    'active': 'wbs',
    'forms': {},
}

@bp_wbs.route('/',methods=['GET'])
@login_required
def index():
    return render_template(wbs_templates['index'],context=context)


@bp_wbs.route('/customers', methods=['GET'])
@login_required
def customer_index():
    pass


@bp_wbs.route('/billings', methods=['GET'])
@login_required
def bill_index():
    pass