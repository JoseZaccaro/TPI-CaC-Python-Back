-- Insertar ciudades
INSERT INTO cities (id_city, name) VALUES
(1, 'Buenos Aires'),
(2, 'Bariloche');

-- Insertar hoteles en Buenos Aires
INSERT INTO hotels (id_hotel, name, address, description, image, id_city) VALUES
(1, 'Hotel Buenos Aires Centro', 'Av. Principal 123', 'Un hotel cómodo y moderno en el centro de Buenos Aires.', 'https://images.pexels.com/photos/323311/pexels-photo-323311.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 1),
(2, 'Hotel Buenos Aires Sur', 'Calle Principal 456', 'Un hotel cerca de la costa sur de Buenos Aires.', 'https://images.pexels.com/photos/4947281/pexels-photo-4947281.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 1);

-- Insertar hoteles en Bariloche
INSERT INTO hotels (id_hotel, name, address, description, image, id_city) VALUES
(3, 'Hotel Bariloche Centro', 'Av. Principal 789', 'Un hotel moderno en el centro de Bariloche con vistas al lago.', 'https://images.pexels.com/photos/452726/pexels-photo-452726.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 2),
(4, 'Hotel Bariloche Ladera', 'Av. Principal 123', 'Un hotel moderno en la ladera del cerro Otto de Bariloche con vistas al lago.', 'https://images.pexels.com/photos/20312005/pexels-photo-20312005/free-photo-of-resfriado-frio-nieve-nevar.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 2);

-- Insertar habitaciones en el Hotel Buenos Aires Centro
INSERT INTO rooms (id_room, type, price, disponibility, image, id_hotel) VALUES
(1, 'Doble', '150', 'true', 'https://cdn.pixabay.com/photo/2020/10/18/09/16/bedroom-5664221_960_720.jpg', 1),
(2, 'Suite', '250', 'true', 'https://cdn.pixabay.com/photo/2016/04/15/11/45/hotel-1330841_960_720.jpg', 1);

-- Insertar habitaciones en el Hotel Buenos Aires Sur
INSERT INTO rooms (id_room, type, price, disponibility, image, id_hotel) VALUES
(3, 'Individual', '100', 'true', 'https://cdn.pixabay.com/photo/2016/11/19/13/06/bed-1839183_960_720.jpg', 2),
(4, 'Doble', '180', 'true', 'https://cdn.pixabay.com/photo/2016/11/19/13/06/bed-1839184_960_720.jpg', 2);

-- Insertar habitaciones en el Hotel Bariloche Centro
INSERT INTO rooms (id_room, type, price, disponibility, image, id_hotel) VALUES
(5, 'Doble con vista al lago', '200', 'true', 'https://cdn.pixabay.com/photo/2017/08/17/11/47/indoor-2650995_960_720.jpg', 3),
(6, 'Suite de lujo', '350', 'true', 'https://cdn.pixabay.com/photo/2016/11/19/13/06/bed-1839183_960_720.jpg', 3);

-- Insertar habitaciones en el Hotel Bariloche Ladera
INSERT INTO rooms (id_room, type, price, disponibility, image, id_hotel) VALUES
(7, 'Doble con vista al lago', '200', 'true', 'https://cdn.pixabay.com/photo/2020/11/24/11/36/bedroom-5772286_960_720.jpg', 4),
(8, 'Suite de lujo', '350', 'true', 'https://cdn.pixabay.com/photo/2016/11/30/08/48/bedroom-1872196_960_720.jpg', 4);