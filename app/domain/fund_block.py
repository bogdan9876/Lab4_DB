from app.app import db


class FundBlock(db.Model):
    __tablename__ = 'fund_block'
    id = db.Column(db.Integer, primary_key=True)
    block_amount = db.Column(db.Float, nullable=False)
    block_date = db.Column(db.Date, nullable=False)
    release_date = db.Column(db.Date)
    status = db.Column(db.Enum('active', 'released'))
    RegistrationConfirmation_id = db.Column(db.Integer, db.ForeignKey('registration_confirmation.id'))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
