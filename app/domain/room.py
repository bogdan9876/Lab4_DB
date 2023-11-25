from app import db


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    room_size = db.Column(db.Float)
    bed_type = db.Column(db.String(50))
    Hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
