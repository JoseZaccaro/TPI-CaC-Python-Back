from flask import Flask
from flask_cors import CORS
from app.routes.cities import *
from app.routes.hotels import *
from app.routes.rooms import *
from app.views import *
from app.routes.reservations import *
from app.database import init_app

#inicializacion del proyecto Flask
app = Flask(__name__)

init_app(app)
CORS(app)


# Rutas para cities
app.route('/', methods=['GET'])(index)
app.route('/api/cities/', methods=['GET'])(get_all_cities)
app.route('/api/cities/<int:city_id>', methods=['GET'])(get_city)
app.route('/api/cities/', methods=['POST'])(create_city)
app.route('/api/cities/<int:city_id>', methods=['PUT'])(update_city)
app.route('/api/cities/<int:city_id>', methods=['DELETE'])(delete_city)

# Rutas para hotels
app.route('/api/hotels/', methods=['GET'])(get_all_hotels)
app.route('/api/hotels/<int:hotel_id>', methods=['GET'])(get_hotel)
app.route('/api/hotels/', methods=['POST'])(create_hotel)
app.route('/api/hotels/<int:hotel_id>', methods=['PUT'])(update_hotel)
app.route('/api/hotels/<int:hotel_id>', methods=['DELETE'])(delete_hotel)


# Rutas para rooms
app.route('/api/rooms/', methods=['GET'])(get_all_rooms)
app.route('/api/rooms/', methods=['POST'])(create_room)
app.route('/api/rooms/<int:room_id>', methods=['PUT'])(update_room)
app.route('/api/rooms/<int:room_id>', methods=['GET'])(get_room)
app.route('/api/rooms/<int:room_id>', methods=['DELETE'])(delete_room)


# Rutas para reservations
app.route('/api/reservations/', methods=['GET'])(get_all_reservations)
app.route('/api/reservations/', methods=['POST'])(create_reservation)
app.route('/api/reservations/<int:reservation_id>', methods=['GET'])(get_reservation)
app.route('/api/reservations/dni/<string:dni>', methods=['GET'])(get_reservations_by_dni)
app.route('/api/reservations/<int:reservation_id>', methods=['DELETE'])(delete_reservation)
app.route('/api/reservations/<int:reservation_id>', methods=['PUT'])(update_reservation)

if __name__=='__main__':
    app.run(debug=True)