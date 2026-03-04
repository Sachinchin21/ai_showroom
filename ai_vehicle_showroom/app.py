from flask import Flask, render_template
from models import db, Vehicle

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showroom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vehicles")
def vehicles():
    all_vehicles = Vehicle.query.all()
    return render_template("vehicles.html", vehicles=all_vehicles)

@app.route("/vehicle/<int:vehicle_id>")
def vehicle_detail(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    # Get related vehicles (same type, excluding current)
    related_vehicles = Vehicle.query.filter(
        Vehicle.vehicle_type == vehicle.vehicle_type,
        Vehicle.id != vehicle.id
    ).limit(3).all()
    return render_template("vehicle_detail.html", vehicle=vehicle, related_vehicles=related_vehicles)


# 🔥 Create DB and insert sample data with real images
with app.app_context():
    db.create_all()

    if Vehicle.query.count() == 0:
        car1 = Vehicle(
            name="Creta",
            brand="Hyundai",
            price=1200000,
            fuel_type="Petrol",
            vehicle_type="SUV",
            image="https://images.unsplash.com/photo-1590362891991-f776e747a588?w=600&q=80"
        )

        car2 = Vehicle(
            name="Swift",
            brand="Maruti",
            price=800000,
            fuel_type="Petrol",
            vehicle_type="Car",
            image="https://images.unsplash.com/photo-1617788138017-80ad40651399?w=600&q=80"
        )

        bike1 = Vehicle(
            name="Royal Enfield Classic 350",
            brand="Royal Enfield",
            price=200000,
            fuel_type="Petrol",
            vehicle_type="Bike",
            image="https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=600&q=80"
        )

        car3 = Vehicle(
            name="Fortuner",
            brand="Toyota",
            price=3500000,
            fuel_type="Diesel",
            vehicle_type="SUV",
            image="https://stimg.cardekho.com/images/carexteriorimages/930x620/Toyota/Fortuner/10904/1755846017683/front-left-side-47.jpg"
            )
        bike2 = Vehicle(
            name="Pulsar NS200",
            brand="Bajaj",
            price=140000,
            fuel_type="Petrol",
            vehicle_type="Bike",
            image="https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=600&q=80"
        )

        car4 = Vehicle(
            name="Baleno",
            brand="Maruti",
            price=700000,
            fuel_type="Petrol",
            vehicle_type="Car",
            image="https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=600&q=80"
        )

        db.session.add_all([car1, car2, bike1, car3, bike2, car4])
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True, port=5001)


