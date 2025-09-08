# API de Biblioteca con Django REST Framework

API RESTful construida con Django y Django REST Framework para gestionar los recursos de una biblioteca, incluyendo autores, libros, editoriales, miembros y préstamos.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Puesta en Marcha](#instalación-y-puesta-en-marcha)
  - [Pre-requisitos](#pre-requisitos)
  - [Pasos de Instalación](#pasos-de-instalación)
- [Documentación de la API (Endpoints)](#documentación-de-la-api-endpoints)
  - [Autores](#autores)
  - [Editoriales](#editoriales)
  - [Libros](#libros)
  - [Miembros](#miembros)
  - [Préstamos](#préstamos)

## Características

- ✅ CRUD completo para **Autores**.
- ✅ CRUD completo para **Editoriales**.
- ✅ CRUD completo para **Libros**.
- ✅ CRUD completo para **Miembros** de la biblioteca.
- ✅ CRUD completo para **Préstamos** de libros.
- ✅ Endpoints de filtrado para libros (por autor y/o editorial).
- ✅ Endpoints de filtrado para préstamos (por miembro o por libro).

## Tecnologías Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Instalación y Puesta en Marcha

Sigue estas instrucciones para tener una copia del proyecto funcionando en tu máquina local.

### Pre-requisitos

- Python 3.8 o superior.
- `pip` y `venv` (generalmente incluidos con Python).

### Pasos de Instalación

1.  **Clona el repositorio**
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2.  **Crea y activa un entorno virtual**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias**
    (Asegúrate de tener un archivo `requirements.txt` en tu proyecto)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones de la base de datos**
    ```bash
    python manage.py migrate
    ```

5.  **Ejecuta el servidor de desarrollo**
    ```bash
    python manage.py runserver
    ```

    La API estará disponible en `http://127.0.0.1:8000/`.

## Documentación de la API (Endpoints)

A continuación se detallan los endpoints disponibles.

---

### Autores

| Método | Endpoint                 | Descripción                      |
| :----- | :----------------------- | :------------------------------- |
| `GET`  | `/api/autores/`          | Lista todos los autores.         |
| `POST` | `/api/autores/crear/`    | Crea un nuevo autor.             |
| `PUT`  | `/api/autores/actualizar/<int:pk>/` | Actualiza un autor existente.    |
| `DELETE`| `/api/autores/eliminar/<int:pk>/`   | Elimina un autor.                |

---

### Editoriales

| Método | Endpoint                 | Descripción                      |
| :----- | :----------------------- | :------------------------------- |
| `GET`  | `/api/editoriales/`      | Lista todas las editoriales.     |
| `POST` | `/api/editoriales/crear/`| Crea una nueva editorial.        |
| `PUT`  | `/api/editoriales/actualizar/<int:pk>/` | Actualiza una editorial existente. |
| `DELETE`| `/api/editoriales/eliminar/<int:pk>/`   | Elimina una editorial.           |

---

### Libros

| Método | Endpoint                 | Descripción                      |
| :----- | :----------------------- | :------------------------------- |
| `GET`  | `/api/libros/`           | Lista todos los libros.          |
| `POST` | `/api/libros/crear/`     | Crea un nuevo libro.             |
| `PUT`  | `/api/libros/actualizar/<int:pk>/` | Actualiza un libro existente.    |
| `DELETE`| `/api/libros/eliminar/<int:pk>/`   | Elimina un libro.                |
| `GET`  | `/api/libros/filtro/autor/<int:autor_id>/` | Filtra libros por autor.         |
| `GET`  | `/api/libros/filtro/editorial/<int:editorial_id>/` | Filtra libros por editorial.     |

---

### Miembros

| Método | Endpoint                 | Descripción                      |
| :----- | :----------------------- | :------------------------------- |
| `GET`  | `/api/miembros/`         | Lista todos los miembros.        |
| `POST` | `/api/miembros/crear/`   | Crea un nuevo miembro.           |
| `PUT`  | `/api/miembros/actualizar/<int:pk>/` | Actualiza un miembro existente.  |
| `DELETE`| `/api/miembros/eliminar/<int:pk>/`   | Elimina un miembro.              |

---

### Préstamos

| Método | Endpoint                 | Descripción                      |
| :----- | :----------------------- | :------------------------------- |
| `GET`  | `/api/prestamos/`        | Lista todos los préstamos.       |
| `POST` | `/api/prestamos/crear/`  | Crea un nuevo préstamo.          |
| `PUT`  | `/api/prestamos/actualizar/<int:pk>/` | Actualiza un préstamo existente. |
| `DELETE`| `/api/prestamos/eliminar/<int:pk>/`   | Elimina un préstamo.             |
| `GET`  | `/api/prestamos/miembro/<int:miembro_id>/` | Lista los préstamos de un miembro. |
| `GET`  | `/api/prestamos/libro/<int:libro_id>/`     | Lista los préstamos de un libro.   |

---

## Colección de Postman

Para facilitar las pruebas de la API, se ha creado una colección de Postman que incluye todos los endpoints documentados.

Ver la documentación y colección de Postman

Url: https://documenter.getpostman.com/view/43047513/2sB3HnJKSF