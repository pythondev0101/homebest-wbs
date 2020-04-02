from app.wbs import bp_wbs
from .models import Customer
from flask_login import login_required
from flask import render_template
from app import context
from . import wbs_templates, wbs_urls


def change_context(view):
    context['module'] = 'wbs'
    if view == 'index':
        context['title'] = 'Water Billing'
        context['active'] = ''
        context['modal'] = True


@bp_wbs.route('/',methods=['GET'])
@login_required
def index():
    change_context('index')
    return render_template(wbs_templates['index'],context=context)


@bp_wbs.route('/customers', methods=['GET'])
@login_required
def customer_index():
    pass


@bp_wbs.route('/billings', methods=['GET'])
@login_required
def bill_index():
    pass