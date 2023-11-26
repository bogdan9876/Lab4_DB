from __future__ import annotations
from typing import Dict, Any
from app import db


class Hotel(db.Model):
    __tablename__ = 'hotel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(250))
    rating = db.Column(db.Float)
    HotelChain_id = db.Column(db.Integer, db.ForeignKey('hotel_chain.id'))
    location = db.relationship("HotelLocation", backref="hotel", uselist=False)

    def __repr__(self) -> str:
        return f"Hotel({self.id}, '{self.name}', '{self.address}', '{self.contact_info}', {self.rating}, {self.HotelChain_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'contact_info': self.contact_info,
            'rating': self.rating,
            'HotelChain_id': self.HotelChain_id,
            'location': self.location.put_into_dto() if self.location else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Hotel:
        hotel = Hotel(
            name=dto_dict.get('name'),
            address=dto_dict.get('address'),
            contact_info=dto_dict.get('contact_info'),
            rating=dto_dict.get('rating'),
            HotelChain_id=dto_dict.get('HotelChain_id')
        )
        return hotel
