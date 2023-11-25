from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Enum('client', 'administrator'), nullable=False)
    date_of_birth = db.Column(db.Date)
    phone_number = db.Column(db.String(15))
