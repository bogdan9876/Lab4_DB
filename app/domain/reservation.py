from app import db


class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('confirmed', 'pending'), nullable=False)
    total_price = db.Column(db.Float)
    payment_method = db.Column(db.Enum('credit_card', 'debit_card', 'cash'))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    FundBlock_id = db.Column(db.Integer, db.ForeignKey('fundblock.id'))
