from __future__ import annotations
from typing import Dict, Any
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
    reviews = db.relationship("Review", backref="user", lazy="dynamic")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', role='{self.role}', " \
               f"date_of_birth={self.date_of_birth}, phone_number='{self.phone_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'phone_number': self.phone_number,
            'reviews': [review.put_into_dto() for review in self.reviews] if self.reviews else []
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        user = User(
            name=dto_dict.get('name'),
            email=dto_dict.get('email'),
            password=dto_dict.get('password'),
            role=dto_dict.get('role'),
            date_of_birth=dto_dict.get('date_of_birth'),
            phone_number=dto_dict.get('phone_number')
        )
        return user
