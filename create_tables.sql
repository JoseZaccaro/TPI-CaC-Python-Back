CREATE TABLE IF NOT EXISTS cities (
    id_city INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS hotels (
    id_hotel INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    description TEXT,
    image TEXT,
    id_city INTEGER,
    FOREIGN KEY (id_city) REFERENCES cities(id_city)
);

CREATE TABLE IF NOT EXISTS rooms (
    id_room INTEGER PRIMARY KEY AUTO_INCREMENT,
    type TEXT NOT NULL,
    price TEXT NOT NULL,
    disponibility TEXT NOT NULL,
    image TEXT,
    id_hotel INTEGER,
    FOREIGN KEY (id_hotel) REFERENCES hotels(id_hotel)
);

CREATE TABLE IF NOT EXISTS reservations (
    id_reservation INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_room INTEGER NOT NULL,
    dni VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    FOREIGN KEY (id_room) REFERENCES rooms(id_room)
);