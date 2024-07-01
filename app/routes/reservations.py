from flask import Blueprint,jsonify, request
from app.models.reservation import Reservation

def get_all_reservations():
    try:
        reservations = Reservation.get_all()
        list_reservations = [reservation.serialize() for reservation in reservations]
        return jsonify(list_reservations)
    except Exception as e:
        print(e)
        return jsonify([])

def create_reservation():
    data = request.json
    new_reservation = Reservation(
        id_room=data['id_room'],
        dni=data['dni'],
        email=data['email'],
        fecha_inicio=data['fecha_inicio'],
        fecha_fin=data['fecha_fin']
    )
    new_reservation.save()
    return jsonify({'message': 'Reservation created'}), 201

def get_reservation(reservation_id):
    reservation = Reservation.get_by_id(reservation_id)
    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404
    return jsonify(reservation.serialize())


def get_reservations_by_dni(dni):
    try:
        reservations = Reservation.get_by_dni(dni)
        list_reservations = [reservation.serialize() for reservation in reservations]
        return jsonify(list_reservations)
    except Exception as identifier:
        print(identifier)
        return jsonify([])
    

def delete_reservation(reservation_id):
    try:
        reservation = Reservation.get_by_id(reservation_id)
        if not reservation:
            return jsonify({'message': 'Reservation not found'}), 404
        reservation.delete()
        return jsonify({'message': 'Reservation deleted successfully'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error deleting reservation'}), 500


reservations_bp = Blueprint('reservations', __name__, url_prefix='/api/reservations')

@reservations_bp.route('/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    data = request.json
    
    # Verificar si la reserva existe
    reservation = Reservation.get_by_id(reservation_id)
    if not reservation:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    
    # Actualizar los campos de la reserva
    reservation.id_room = data.get('id_room', reservation.id_room)
    reservation.dni = data.get('dni', reservation.dni)
    reservation.email = data.get('email', reservation.email)
    reservation.fecha_inicio = data.get('fecha_inicio', reservation.fecha_inicio)
    reservation.fecha_fin = data.get('fecha_fin', reservation.fecha_fin)
    
    try:
        reservation.save()  # Guardar los cambios en la base de datos
        return jsonify({'message': 'Reserva actualizada exitosamente'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Error al actualizar la reserva'}), 500