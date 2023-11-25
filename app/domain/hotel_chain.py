from app import db


class HotelChain(db.Model):
    __tablename__ = 'hotel_chain'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100))
    established_year = db.Column(db.Integer)
    owner_name = db.Column(db.String(50))
    number_of_hotels = db.Column(db.Integer)
