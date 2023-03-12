from . import db

class Property(db.Model):
    __tablename__='propertytable'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    num_bedrooms = db.Column(db.Integer, nullable=False)
    num_bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    photo_filename = db.Column(db.String(100), nullable=False)

    def __init__(self, title, type, num_bedrooms, num_bathrooms, location, price, description, photo_filename):
        self.title = title
        self.type = type
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.location = location
        self.price = price
        self.description = description
        self.photo_filename = photo_filename