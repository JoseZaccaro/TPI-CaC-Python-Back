from app.database import get_db
class Hotel:

    #constuctor
    def __init__(self,id_hotel=None,name=None,address=None,description=None,image=None,id_city=None):
        self.id_hotel=id_hotel
        self.name=name
        self.address=address
        self.description=description
        self.image=image
        self.id_city=id_city

    def serialize(self):
        return {
            'id_hotel': self.id_hotel,
            'name': self.name,
            'address': self.address,
            'description': self.description,
            'image': self.image,
            'id_city': self.id_city
        }
        
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM hotels"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        # hotels = [Hotel(id_hotel=row[0], name=row[1], address=row[2], description=row[3], image=row[4], id_city=row[5]) for row in rows]

        hotels = []
        for row in rows:
            new_hotel = Hotel(id_hotel=row[0], name=row[1], address=row[2], description=row[3], image=row[4], id_city=row[5])
            hotels.append(new_hotel)

        cursor.close()
        return hotels
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO hotels (name, address, description, image, id_city) VALUES (%s, %s, %s, %s, %s)
        """, (self.name, self.address, self.description, self.image, self.id_city))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM hotels WHERE id_hotel = %s", (self.id_hotel,))
        db.commit()
        cursor.close()

    def update(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            UPDATE hotels
            SET name = %s, address = %s, description = %s, image = %s, id_city = %s
            WHERE id_hotel = %s
        """, (self.name, self.address, self.description, self.image, self.id_city, self.id_hotel))
        db.commit()
        cursor.close()
        
    def get_by_id(hotel_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hotels WHERE id_hotel = %s", (hotel_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Hotel(id_hotel=row[0], name=row[1], address=row[2], description=row[3], image=row[4], id_city=row[5])
        return None
    
    def get_by_city(city_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hotels WHERE id_city = %s", (city_id,))
        rows = cursor.fetchall() #Me devuelve un lista de tuplas
        cursor.close()
        return rows
    
    def get_by_name(name):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hotels WHERE name = %s", (name,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Hotel(id_hotel=row[0], name=row[1], address=row[2], description=row[3], image=row[4], id_city=row[5])
        return None
    