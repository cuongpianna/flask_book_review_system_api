from werkzeug.security import generate_password_hash,check_password_hash

from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(255))
    address = db.Column(db.String(255),nullable=True,default='')
    avartar = db.Column(db.String(255),nullable=True,default='')

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)