from app.app import db


class Availability(db.Model):
    __tablename__ = 'availability'
    id = db.Column(db.Integer, primary_key=True)
    booking_start_date = db.Column(db.Date, nullable=False)
    booking_start_end = db.Column(db.Date, nullable=False)
    guest_count = db.Column(db.Integer)
    is_weekend = db.Column(db.Boolean)
    Room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
