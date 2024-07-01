from flask import jsonify, request
from app.models.room import Room

def get_all_rooms():
    try:
        rooms = Room.get_all()
        list_rooms = [room.serialize() for room in rooms]
        return jsonify(list_rooms)
    except Exception as e:
        print(e)
        return jsonify([])

def create_room():
    data = request.json
    new_room = Room(
        name=data['name'],
        type=data['type'],
        price=data['price'],
        disponibility=data['disponibility'],
        image=data['image'],
        id_hotel=data['id_hotel']
    )
    new_room.save()
    return jsonify({'message': 'Room created'}), 201

def update_room(room_id):
    room = Room.get_by_id(room_id)
    if not room:
        return jsonify({'message': 'Room not found'}), 404
    data = request.json
    room.name = data['name']
    room.type = data['type']
    room.price = data['price']
    room.disponibility = data['disponibility']
    room.image = data['image']
    room.id_hotel = data['id_hotel']
    room.update()
    return jsonify({'message': 'Room updated successfully'})

def get_room(room_id):
    room = Room.get_by_id(room_id)
    if not room:
        return jsonify({'message': 'Room not found'}), 404
    return jsonify(room.serialize())

def delete_room(room_id):
    room = Room.get_by_id(room_id)
    if not room:
        return jsonify({'message': 'Room not found'}), 404
    room.delete()
    return jsonify({'message': 'Room deleted successfully'})
