from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_login import LoginManager

db = SQLAlchemy()
r = FlaskRedis()
login_manager = LoginManager()
login_manager.login_view = 'bp_auth.login'

# TODO: FOR FUTURE change this to automatic values eg. system_models=[USER OBJECT]
""" EDITABLE: IMPORT HERE THE SYSTEM MODULES and their models/attributes """
system_modules = {'Administrator':
                      {'icon': 'fa-home', 'link': 'bp_admin.index',
                       'models': {
                           'Users': {'icon': 'fa-users', 'functions': {'View users': 'bp_auth.index'}}}},
                  'Water Billing':
                       {'icon': 'fa-tint', 'link': 'bp_wbs.index',
                        'models': {
                            'Customers': {'icon': 'fa-users', 'functions': {'View customers': 'bp_auth.index'}},
                            'Billing': {'icon': 'fa-usd', 'functions': {'View customers': 'bp_auth.index'}},
                            'Payments': {'icon': 'fa-money', 'functions': {'View customers': 'bp_auth.index'}}}
                        }
                  }


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    r.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        """EDITABLE: IMPORT HERE THE SYSTEM MODULES  """
        from app import core
        from app import auth
        from app import admin
        from app import wbs
        """--------------END--------------"""

        """EDITABLE: REGISTER HERE THE MODULE BLUEPRINTS"""
        app.register_blueprint(core.bp_core, url_prefix='/')
        app.register_blueprint(auth.bp_auth, url_prefix='/auth')
        app.register_blueprint(admin.bp_admin, url_prefix='/admin')
        app.register_blueprint(wbs.bp_wbs, url_prefix='/wbs')
        """--------------END--------------"""

        db.create_all()
        return app


# GLOBAL APP INSTANCE
app = create_app()
