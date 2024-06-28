CREATE TABLE IF NOT EXISTS cities (
    id_city INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    hotels TEXT
);

CREATE TABLE IF NOT EXISTS hotels (
    id_hotel INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    description TEXT,
    image TEXT,
    habitaciones TEXT
);

CREATE TABLE IF NOT EXISTS rooms (
    id_room INTEGER PRIMARY KEY AUTO_INCREMENT,
    type TEXT NOT NULL,
    price TEXT NOT NULL,
    disponibility TEXT NOT NULL,
    image TEXT
);
