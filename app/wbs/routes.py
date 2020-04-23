from app.wbs import bp_wbs
from .models import Bill, Customer
from flask_login import login_required
from flask import render_template, request, current_app, url_for
from app import context
from . import wbs_templates, wbs_urls
from .forms import BillCreateForm
from app.admin.routes import admin_index, admin_edit


context['module'] = 'wbs'

@bp_wbs.route('/billing',methods=['GET'])
@login_required
def index():
    form = BillCreateForm()
    fields = [Bill.id,Bill.customer_id,Bill.meter_no,Bill.amount_due,Bill.period_from,Bill.period_to]
    return admin_index(Bill,fields=fields, form=form,url=wbs_urls['index'],create_modal=False,template="wbs/wbs_index.html")


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
