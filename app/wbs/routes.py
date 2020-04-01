from app.wbs import bp_wbs
from .models import Customer
from flask_login import login_required


@bp_wbs.route('/customers', methods=['GET'])
@login_required
def customer_index():
    pass


@bp_wbs.route('/billings', methods=['GET'])
@login_required
def bill_index():
    pass