from app.app import db


class HotelLocation(db.Model):
    __tablename__ = 'hotel_location'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    Hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
