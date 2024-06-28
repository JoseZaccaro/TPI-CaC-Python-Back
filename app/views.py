from flask import jsonify, request
from app.models.city import City

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