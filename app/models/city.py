from app.database import get_db
class City:

    #constuctor
    def __init__(self,id_city=None,name=None,hotels=None):
        self.id_city=id_city
        self.name=name
        self.hotels=hotels
    
    def serialize(self):
        return {
            'id_city': self.id_city,
            'name': self.name,
            'hotels': self.hotels
        }


    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM cities"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        # cities = [City(id_city=row[0], name=row[1], hotels=row[2]) for row in rows]

        cities = []
        for row in rows:
            new_city = City(id_city=row[0], name=row[1], hotels=row[2])
            cities.append(new_city)

        cursor.close()
        return cities
    
    @staticmethod
    def get_by_id(city_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cities WHERE id_city = %s", (city_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return City(id_city=row[0], name=row[1], hotels=row[2])
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO cities (name, hotels) VALUES (%s, %s)
        """, (self.name, self.hotels))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM cities WHERE id_city = %s", (self.id_city,))
        db.commit()
        cursor.close()

