from app.app import db


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String(1000))
    rating = db.Column(db.Float)
    visit_date = db.Column(db.Date)
    service_quality = db.Column(db.Enum('poor', 'average', 'good', 'excellent'))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
