from app.database import get_db
class Room:

    #constuctor
    def __init__(self,id_room=None,type=None,price=None,disponibility=None, image=None):
        self.id_room=id_room
        self.type=type
        self.price=price
        self.disponibility=disponibility
        self.image=image

    def serialize(self):
        return {
            'id_room': self.id_room,
            'type': self.type,
            'price': self.price,
            'disponibility': self.disponibility,
            'image': self.image
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
            new_room = Room(id_room=row[0], type=row[1], price=row[2], disponibility=row[3], image=row[4])
            rooms.append(new_room)

        cursor.close()
        return rooms
    