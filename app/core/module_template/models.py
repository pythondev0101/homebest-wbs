# """ MODELS """
# """ FLASK IMPORTS """
# from flask_login import UserMixin
#
# """--------------END--------------"""
#
# """ PYTHON IMPORTS """
# from werkzeug.security import generate_password_hash, check_password_hash
#
# """--------------END--------------"""
#
# """ APP IMPORTS  """
# from app import db
# from app.core.models import Base
# """--------------END--------------"""
#
#
# # Sample model
# class User(UserMixin, Base):
#     __tablename__ = 'auth_user'
#
#     username = db.Column(db.String(64), nullable=False, index=True, unique=True)
#     fname = db.Column(db.String(64), nullable=False, server_default="")
#     lname = db.Column(db.String(64), nullable=False, server_default="")
#     email = db.Column(db.String(64), nullable=False, unique=True)
#     password_hash = db.Column(db.String(128), nullable=False)
#     image_path = db.Column(db.String(64),nullable=False)
#
#     def __init__(self):
#         Base.__init__(self)
#         self.image_path = "img/user_default_image.png"
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     def __repr__(self):
#         return "<User {}>".format(self.username)
#
