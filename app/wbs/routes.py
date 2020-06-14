from app.wbs import bp_wbs
from flask_login import login_required
from flask import render_template, request, current_app, url_for,redirect,flash
from app import context,db
from .forms import BillCreateForm, CustomerCreateForm,PaymentCreateForm,CustomerEditForm, \
    BillEditForm,PaymentEditForm,PaymentTypeCreateForm
from app.admin.routes import admin_index, admin_edit
from .models import Bill, Customer,Payment,PaymentType



@bp_wbs.route('/billing',methods=['GET'])
@login_required
def index():
    form = BillCreateForm()
    fields = [Bill.id,Bill.id,Customer.lname,Bill.meter_no,Bill.amount_due,Bill.period_from,Bill.period_to]
    models = [Bill,Customer]
    return admin_index(*models,fields=fields, form=form,url='bp_wbs.index', \
        create_url='bp_wbs.bill_create',edit_url="bp_wbs.bill_edit",template="wbs/wbs_index.html")


@bp_wbs.route('/bill_create',methods=['POST'])
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
            bill.previous_reading = form.previous_reading.data
            bill.present_reading = form.present_reading.data
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
        create_url='bp_wbs.customer_create',edit_url="bp_wbs.customer_edit",template="wbs/wbs_index.html")


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
    fields = [Payment.id,Bill.id,Customer.fname,Payment.payment_date,Payment.amount_paid]
    models = [Payment,Customer]
    return admin_index(*models,fields=fields,url='bp_wbs.payment_index',form=form, \
        create_url="bp_wbs.payment_create",edit_url="bp_wbs.payment_edit",template='wbs/wbs_index.html')

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
            if not form.payment_type_id.data:
                payment.payment_type_id = None
            else:
                payment.payment_type_id = form.payment_type_id.data
            payment.amount_paid = form.amount_paid.data
            db.session.add(payment)
            db.session.commit()
            flash('Payment successfully added!','success')
            return redirect(url_for('bp_wbs.payment_index'))
        else:
            for key,value in form.errors.items():
                flash(str(key) + str(value),'error')
            return redirect(url_for('bp_wbs.payment_index'))


@bp_wbs.route("/customer_edit/<int:oid>",methods=['GET','POST'])
@login_required
def customer_edit(oid):
    customer = Customer.query.get_or_404(oid)
    form = CustomerEditForm(obj=customer)
    if request.method == "GET":
        billings = Bill.query.filter_by(customer_id=oid).all()
        form.billing_inline.models = billings
        payments = Payment.query.filter_by(customer_id=oid).all()
        form.payment_inline.models = payments
        return admin_edit(form=form,update_url="bp_wbs.customer_edit",oid=oid,model=Customer,template="wbs/wbs_edit.html")
    elif request.method == "POST":
        customer.fname = form.fname.data
        customer.lname = form.lname.data
        customer.phone = form.phone.data
        customer.email = form.email.data
        customer.zip = form.zip.data
        customer.street = form.street.data
        customer.city_id = form.city_id.data
        customer.province_id = form.province_id.data
        db.session.commit()
        flash('Customer updated successfully!','success')
        return redirect(url_for('bp_wbs.customer_index'))


@bp_wbs.route('/bill_edit/<int:oid>',methods=['GET','POST'])
@login_required
def bill_edit(oid):
    bill = Bill.query.get_or_404(oid)
    form = BillEditForm(obj=bill)
    if request.method == "GET":
        return admin_edit(form=form,update_url="bp_wbs.bill_edit",oid=oid,model=Bill,template="wbs/wbs_edit.html")
    elif request.method == "POST":
        bill.meter_no = form.meter_no.data
        bill.customer_id = form.customer_id.data
        bill.amount_due = form.amount_due.data
        bill.due_date = form.due_date.data
        bill.period_from = form.period_from.data
        bill.period_to = form.period_to.data
        db.session.commit()
        flash("Bill updated successfully!",'success')
        return redirect(url_for("bp_wbs.index"))

@bp_wbs.route('/payment_edit/<int:oid>',methods=['GET','POST'])
@login_required
def payment_edit(oid):
    payment = Payment.query.get_or_404(oid)
    form = PaymentEditForm(obj=payment)
    if request.method == 'GET':
        return admin_edit(form=form,update_url='bp_wbs.payment_edit',oid=oid,model=Payment,template="wbs/wbs_edit.html")

@bp_wbs.route("/payment_types")
@login_required
def payment_types():
    form = PaymentTypeCreateForm()
    fields = [PaymentType.id,PaymentType.name,PaymentType.created_at]
    return admin_index(PaymentType,fields=fields,url="bp_wbs.payment_types",form=form, \
        view_modal=False,template="wbs/wbs_index.html",create_url="bp_wbs.payment_type_create")

@bp_wbs.route("/payment_type_create",methods=["POST"])
@login_required
def payment_type_create():
    form = PaymentTypeCreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            payment_type = PaymentType()
            payment_type.name = form.name.data
            db.session.add(payment_type)
            db.session.commit()
            flash("Payment Type added successfully!",'success')
            return redirect(url_for('bp_wbs.payment_types'))
        else:
            for key,value in form.errors.items():
                flash(str(key) + str(value),'error')
            return redirect(url_for('bp_wbs.payment_types'))