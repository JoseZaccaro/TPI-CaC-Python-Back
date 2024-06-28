from flask import jsonify, request
from app.models.city import City
from app.models.hotel import Hotel

def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

def get_all_cities():
    try:
        cities = City.get_all()
        list_cities = [city.serialize() for city in cities]
        return jsonify(list_cities)
    except Exception as identifier:
        print(identifier)
        return jsonify([])

def create_city():
    #recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    new_city = City(
        name = data['name'],
    )
    new_city.save()
    return jsonify({'message':'City created'}), 201
    
def update_city(city_id):
    city = City.get_by_id(city_id)
    if not city:
        return jsonify({'message': 'City not found'}), 404
    data = request.json
    city.name = data['name']
    city.hotels = data['hotels']
    city.save()
    return jsonify({'message': 'City updated successfully'})

def get_city(city_id):
    city = City.get_by_id(city_id)
    if not city:
        return jsonify({'message': 'City not found'}), 404
    return jsonify(city.serialize())

def delete_city(city_id):
    city = City.get_by_id(city_id)
    if not city:
        return jsonify({'message': 'City not found'}), 404
    city.delete()
    return jsonify({'message': 'City deleted successfully'})

def get_all_hotels():
    try:
        hotels = Hotel.get_all()
        list_hotels = [hotel.serialize() for hotel in hotels]
        return jsonify(list_hotels)
    except Exception as identifier:
        print(identifier)
        return jsonify([])

def create_hotel():
    #recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    new_hotel = Hotel(
        name = data['name'],
        address = data['address'],
        description = data['description'],
        image = data['image'],
        id_city = data['id_city'],
    )
    new_hotel.save()
    return jsonify({'message':'Hotel created'}), 201
    
def update_hotel(hotel_id):
    hotel = Hotel.get_by_id(hotel_id)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404
    data = request.json
    hotel.name = data['name']
    hotel.address = data['address']
    hotel.description = data['description']
    hotel.image = data['image']
    hotel.id_city = data['id_city']
    hotel.save()
    return jsonify({'message': 'Hotel updated successfully'})

def get_hotel(hotel_id):
    hotel = Hotel.get_by_id(hotel_id)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404
    return jsonify(hotel.serialize())

def delete_hotel(hotel_id):
    hotel = Hotel.get_by_id(hotel_id)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404
    hotel.delete()
    return jsonify({'message': 'Hotel deleted successfully'})
