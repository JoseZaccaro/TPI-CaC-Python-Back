from app.database import get_db

class Reservation:
    def __init__(self, id_reservation=None, id_room=None, dni=None, email=None, fecha_inicio=None, fecha_fin=None):
        self.id_reservation = id_reservation
        self.id_room = id_room
        self.dni = dni
        self.email = email
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def serialize(self):
        return {
            'id_reservation': self.id_reservation,
            'id_room': self.id_room,
            'dni': self.dni,
            'email': self.email,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin
        }

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_reservation is None:
            # Si el id_reservation es None, se trata de una nueva reserva
            cursor.execute("""
                INSERT INTO reservations (id_room, dni, email, fecha_inicio, fecha_fin) 
                VALUES (%s, %s, %s, %s, %s)
            """, (self.id_room, self.dni, self.email, self.fecha_inicio, self.fecha_fin))
        else:
            # Si el id_reservation existe, se trata de actualizar la reserva
            cursor.execute("""
                UPDATE reservations
                SET id_room = %s, dni = %s, email = %s, fecha_inicio = %s, fecha_fin = %s
                WHERE id_reservation = %s
            """, (self.id_room, self.dni, self.email, self.fecha_inicio, self.fecha_fin, self.id_reservation))
        
        db.commit()
        cursor.close()

    @staticmethod
    def get_by_id(reservation_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservations WHERE id_reservation = %s", (reservation_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reservation(id_reservation=row[0], id_room=row[1], dni=row[2], email=row[3], fecha_inicio=row[4], fecha_fin=row[5])
        return None

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservations")
        rows = cursor.fetchall()
        cursor.close()

        reservations = []
        for row in rows:
            reservation = Reservation(id_reservation=row[0], id_room=row[1], dni=row[2], email=row[3], fecha_inicio=row[4], fecha_fin=row[5])
            reservations.append(reservation)

        return reservations


    @staticmethod
    def get_by_dni(dni):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservations WHERE dni = %s", (dni,))
        rows = cursor.fetchall()
        cursor.close()

        reservations = []
        for row in rows:
            reservation = Reservation(id_reservation=row[0], id_room=row[1], dni=row[2], email=row[3], fecha_inicio=row[4], fecha_fin=row[5])
            reservations.append(reservation)

        return reservations
    

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reservations WHERE id_reservation = %s", (self.id_reservation,))
        db.commit()
        cursor.close()