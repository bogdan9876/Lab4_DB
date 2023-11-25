from app import db


class Hotel(db.Model):
    __tablename__ = 'hotel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(250))
    rating = db.Column(db.Float)
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    HotelChain_id = db.Column(db.Integer, db.ForeignKey('hotel_chain.id'))
