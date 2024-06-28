from app.database import get_db
class City:

    #constuctor
    def __init__(self,id_city=None,name=None):
        self.id_city=id_city
        self.name=name
    
    def serialize(self):
        return {
            'id_city': self.id_city,
            'name': self.name,
        }


    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM cities"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        # cities = [City(id_city=row[0], name=row[1]) for row in rows]

        cities = []
        for row in rows:
            new_city = City(id_city=row[0], name=row[1])
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
            return City(id_city=row[0], name=row[1])
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO cities (name) VALUES (%s)
        """, (self.name))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM cities WHERE id_city = %s", (self.id_city,))
        db.commit()
        cursor.close()

    def update(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            UPDATE cities
            SET name = %s
            WHERE id_city = %s
        """, (self.name, self.id_city))
        db.commit()
        cursor.close()
        
    def get_by_name(name):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cities WHERE name = %s", (name,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return City(id_city=row[0], name=row[1])
        return None
