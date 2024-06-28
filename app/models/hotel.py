from app.database import get_db
class Hotel:

    #constuctor
    def __init__(self,id_hotel=None,name=None,address=None,description=None,image=None,habitaciones=None):
        self.id_hotel=id_hotel
        self.name=name
        self.address=address
        self.description=description
        self.image=image
        self.habitaciones=habitaciones

    def serialize(self):
        return {
            'id_hotel': self.id_hotel,
            'name': self.name,
            'address': self.address,
            'description': self.description,
            'image': self.image,
            'habitaciones': self.habitaciones
        }
        
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM hotels"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        # hotels = [Hotel(id_hotel=row[0], name=row[1], address=row[2], description=row[3], image=row[4], habitaciones=row[5]) for row in rows]

        hotels = []
        for row in rows:
            new_hotel = Hotel(id_hotel=row[0], name=row[1], address=row[2], description=row[3], image=row[4], habitaciones=row[5])
            hotels.append(new_hotel)

        cursor.close()
        return hotels
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO hotels (name, address, description, image, habitaciones) VALUES (%s, %s, %s, %s, %s)
        """, (self.name, self.address, self.description, self.image, self.habitaciones))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM hotels WHERE id_hotel = %s", (self.id_hotel,))
        db.commit()
        cursor.close()


