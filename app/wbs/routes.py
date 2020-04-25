from app.wbs import bp_wbs
from flask_login import login_required
from flask import render_template, request, current_app, url_for,redirect,flash
from app import context,db
from .forms import BillCreateForm, CustomerCreateForm,PaymentCreateForm
from app.admin.routes import admin_index, admin_edit
from .models import Bill, Customer,Payment



@bp_wbs.route('/billing',methods=['GET'])
@login_required
def index():
    form = BillCreateForm()
    fields = [Bill.id,Bill.id,Bill.meter_no,Bill.customer_id,Bill.amount_due,Bill.period_from,Bill.period_to]
    return admin_index(Bill,fields=fields, form=form,url='bp_wbs.index', \
        create_url='bp_wbs.bill_create',template="wbs/wbs_index.html",view_modal=False)


@bp_wbs.route('/bill_create',methods=['GET','POST'])
@login_required
def bill_create():
    form = BillCreateForm()
    if request.method == "POST":
        if form.validate_on_submit():
            bill = Bill()
            bill.meter_no = form.meter_no.data
            bill.customer_id = form.customer_id.data
            bill.amount_due = form.amount_due.data
            bill.due_date = form.due_date.data
            bill.period_from = form.period_from.data
            bill.period_to = form.period_to.data
            db.session.add(bill)
            db.session.commit()
            flash("Bill successfully created!",'success')
            return redirect(url_for('bp_wbs.index'))
        else:
            for key,value in form.errors.items():
                flash(str(key) + str(value),'error')
            return redirect(url_for('bp_wbs.index'))



@bp_wbs.route('/customers', methods=['GET'])
@login_required
def customer_index():
    form = CustomerCreateForm()
    fields = [Customer.id,Customer.fname,Customer.lname,Customer.phone,Customer.email]
    return admin_index(Customer,fields=fields, form=form,url="bp_wbs.customer_index", \
        create_url='bp_wbs.customer_create',view_modal=None,template="wbs/wbs_index.html")


@bp_wbs.route('/customer_create',methods=['POST'])
@login_required
def customer_create():
    form = CustomerCreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            customer = Customer()
            customer.fname = form.fname.data
            customer.lname = form.lname.data
            customer.email = form.email.data
            customer.phone = form.phone.data
            customer.street = form.street.data
            customer.city_id = form.city_id.data
            customer.province_id = form.province_id.data
            customer.zip = form.zip.data
            db.session.add(customer)
            db.session.commit()
            flash('Customer successfully added!','success')
            return redirect(url_for('bp_wbs.customer_index'))
        else:
            for key, value in form.errors.items():
                flash(str(key) + str(value),'error')
            return redirect(url_for('bp_wbs.customer_index'))
            

@bp_wbs.route('/payments',methods=['GET'])
@login_required
def payment_index():
    form = PaymentCreateForm()
    fields = [Payment.id,Payment.bill,Payment.customer,Payment.payment_date,Payment.amount_paid]
    return admin_index(Payment,fields=fields,url='bp_wbs.payment_index',form=form,view_modal=False, \
        create_url="bp_wbs.payment_create",template='wbs/wbs_index.html')

@bp_wbs.route('/payment_create',methods=['GET','POST'])
@login_required
def payment_create():
    form = PaymentCreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            payment = Payment()
            payment.bill_id =form.bill_id.data
            payment.customer_id = form.customer_id.data
            payment.payment_date = form.payment_date.data
            payment.amount_paid = form.amount_paid.data
            db.session.add(payment)
            db.session.commit()
            return redirect(url_for('bp_wbs.payment_index'))
        else:
            for key,value in form.errors.items():
                flash(str(key) + str(value),'error')
            return redirect(url_for('bp_wbs.payment_index'))
