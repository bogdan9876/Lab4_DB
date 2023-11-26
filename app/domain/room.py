from __future__ import annotations
from typing import Dict, Any
from app import db


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    room_size = db.Column(db.Float)
    bed_type = db.Column(db.String(50))
    Hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    availability = db.relationship("Availability", backref="room", uselist=False)

    def __repr__(self) -> str:
        return f"Room({self.id}, '{self.room_type}', {self.price_per_night}, {self.room_size}, '{self.bed_type}', {self.Hotel_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'room_type': self.room_type,
            'price_per_night': self.price_per_night,
            'room_size': self.room_size,
            'bed_type': self.bed_type,
            'Hotel_id': self.Hotel_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Room:
        room = Room(
            room_type=dto_dict.get('room_type'),
            price_per_night=dto_dict.get('price_per_night'),
            room_size=dto_dict.get('room_size'),
            bed_type=dto_dict.get('bed_type'),
            Hotel_id=dto_dict.get('Hotel_id')
        )
        return room
