from app.database import get_db
class Room:

    #constuctor
    def __init__(self,id_room=None,type=None,price=None,disponibility=None, image=None, id_hotel=None):
        self.id_room=id_room
        self.type=type
        self.price=price
        self.disponibility=disponibility
        self.image=image
        self.id_hotel=id_hotel

    def serialize(self):
        return {
            'id_room': self.id_room,
            'type': self.type,
            'price': self.price,
            'disponibility': self.disponibility,
            'image': self.image,
            'id_hotel': self.id_hotel
        }

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM rooms"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        # rooms = [Room(id_room=row[0], type=row[1], price=row[2], disponibility=row[3], image=row[4]) for row in rows]

        rooms = []
        for row in rows:
            new_room = Room(id_room=row[0], type=row[1], price=row[2], disponibility=row[3], image=row[4], id_hotel=row[5])
            rooms.append(new_room)

        cursor.close()
        return rooms
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO rooms (type, price, disponibility, image, id_hotel) VALUES (%s, %s, %s, %s, %s)
        """, (self.type, self.price, self.disponibility, self.image, self.id_hotel))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM rooms WHERE id_room = %s", (self.id_room,))
        db.commit()
        cursor.close()
    
    def update(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            UPDATE rooms SET type = %s, price = %s, disponibility = %s, image = %s, id_hotel = %s WHERE id_room = %s
        """, (self.type, self.price, self.disponibility, self.image, self.id_hotel, self.id_room))
        db.commit()
        cursor.close()
    
    def get_by_id(room_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM rooms WHERE id_room = %s", (room_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Room(id_room=row[0], type=row[1], price=row[2], disponibility=row[3], image=row[4], id_hotel=row[5])
        return None
    
    def get_by_hotel(hotel_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM rooms WHERE id_hotel = %s", (hotel_id,))
        rows = cursor.fetchall()
        cursor.close()
        rooms = []
        for row in rows:
            new_room = Room(id_room=row[0], type=row[1], price=row[2], disponibility=row[3], image=row[4], id_hotel=row[5])
            rooms.append(new_room)
        return rooms
    
    def get_by_disponibility(disponibility):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM rooms WHERE disponibility = %s", (disponibility,))
        rows = cursor.fetchall()
        cursor.close()
        rooms = []
        for row in rows:
            new_room = Room(id_room=row[0], type=row[1], price=row[2], disponibility=row[3], image=row[4], id_hotel=row[5])
            rooms.append(new_room)
        return rooms
    
    def get_by_price(price):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM rooms WHERE price = %s", (price,))
        rows = cursor.fetchall()
        cursor.close()
        rooms = []
        for row in rows:
            new_room = Room(id_room=row[0], type=row[1], price=row[2], disponibility=row[3], image=row[4], id_hotel=row[5])
            rooms.append(new_room)
        return rooms