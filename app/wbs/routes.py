from app.wbs import bp_wbs
from .models import Bill, Customer
from flask_login import login_required
from flask import render_template, request, current_app, url_for
from app import context
from . import wbs_templates, wbs_urls
from .forms import BillCreateForm


def change_context(view):
    context['module'] = 'wbs'
    if view == 'index':
        context['title'] = 'Water Billing'
        context['active'] = 'Billing'
        context['modal'] = True
    if view == 'customer_index':
        context['title'] = 'Water Billing'
        context['active'] = 'Customers'
        context['modal'] = True


@bp_wbs.route('/billing',methods=['GET'])
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    data_per_page = current_app.config['DATA_PER_PAGE']
    bills = Bill.query.paginate(page, data_per_page, False)
    bill_create_form = BillCreateForm()
    next_url = url_for(wbs_urls['index'], page=bills.next_num) \
        if bills.has_next else None
    prev_url = url_for(wbs_urls['index'], page=bills.prev_num) \
        if bills.has_prev else None
    customers = Customer.query.all()

    # ADDITIONAL CONTEXT
    context['bills'] = bills.items
    context['forms'] = {'BillCreateForm': bill_create_form}
    context['next_url'] = next_url
    context['prev_url'] = prev_url
    context['data_per_page'] = data_per_page
    context['customers'] = customers
    change_context('index')
    return render_template(wbs_templates['index'],context=context)


@bp_wbs.route('/customers', methods=['GET'])
@login_required
def customer_index():
    page = request.args.get('page', 1, type=int)
    data_per_page = current_app.config['DATA_PER_PAGE']
    customers = Customer.query.paginate(page, data_per_page, False)
    next_url = url_for(wbs_urls['customer_index'], page=customers.next_num) \
        if customers.has_next else None
    prev_url = url_for(wbs_urls['customer_index'], page=customers.prev_num) \
        if customers.has_prev else None

    # ADDITIONAL CONTEXT
    context['customers'] = customers.items
    context['next_url'] = next_url
    context['prev_url'] = prev_url
    context['data_per_page'] = data_per_page
    change_context('customer_index')
    return render_template(wbs_templates['customer_index'], context=context)
