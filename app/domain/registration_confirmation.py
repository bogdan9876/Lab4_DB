from app.app import db


class RegistrationConfirmation(db.Model):
    __tablename__ = 'registration_confirmation'
    id = db.Column(db.Integer, primary_key=True)
    send_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('confirmed', 'pending'), nullable=False)
    confirmation_code = db.Column(db.String(20))
    expiration_date = db.Column(db.Date)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
