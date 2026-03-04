from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Vehicle {self.name}>"
