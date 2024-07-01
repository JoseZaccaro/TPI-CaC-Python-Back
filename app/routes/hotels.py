from flask import jsonify, request
from app.models.hotel import Hotel


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


def get_all_hotels():
    try:
        city_id = request.args.get('city_id')
        if city_id:
            hotels = Hotel.get_by_city_id(city_id)
        else:
            hotels = Hotel.get_all()
        list_hotels = [hotel.serialize() for hotel in hotels]
        return jsonify(list_hotels)
    except Exception as e:
        print(e)
        return jsonify([])