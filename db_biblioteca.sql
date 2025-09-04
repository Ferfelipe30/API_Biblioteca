-- Tabla: Autor
CREATE TABLE autor (
	id_autor SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	apellido VARCHAR(100) NOT NULL,
	biografia TEXT
);

-- TABLA: editorial
CREATE TABLE editorial (
	id_editorial SERIAL PRIMARY KEY,
	nombre VARCHAR(150) NOT NULL,
	direccion VARCHAR(200) NOT NULL,
	telefono VARCHAR(20)
);

-- TABLA: Libro
CREATE TABLE libro (
	id_libro SERIAL PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	resumen TEXT,
	isbn VARCHAR(20) UNIQUE NOT NULL,
	anio_publicacion INT,
	id_autor INT NOT NULL,
	id_editorial INT NOT NULL,
	CONSTRAINT fk_libro_autor FOREIGN KEY (id_autor) REFERENCES autor(id_autor) ON DELETE CASCADE,
	CONSTRAINT fk_libro_editorial FOREIGN KEY (id_editorial) REFERENCES editorial(id_editorial) ON DELETE CASCADE
);

--TABLA: Miembro
CREATE TABLE miembro (
	id_miembro SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	apellido VARCHAR(100) NOT NULL,
	email VARCHAR(150) NOT NULL,
	fecha_membresia DATE NOT NULL
);

--TABLA: PRESTAMO
CREATE TABLE prestamo (
	id_prestamo SERIAL PRIMARY KEY,
	fecha_prestam DATE NOT NULL,
	fecha_devolucion DATE,
	id_libro INT NOT NULL,
	id_miembro INT NOT NULL,
	CONSTRAINT fk_prestamo_libro FOREIGN KEY (id_libro) REFERENCES libro(id_libro) ON DELETE CASCADE,
	CONSTRAINT fk_prestamo_miembro FOREIGN KEY (id_miembro) REFERENCES miembro(id_miembro) ON DELETE CASCADE
);

