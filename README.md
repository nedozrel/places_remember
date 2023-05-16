# [Places Remember](https://placesremember.na4u.ru/)

Places Remember is a Django website where you can add your places you have been to.

## Installation

There are two options to run the project: manual and using docker-compose.

### Manual installation

1. Clone the repository.

```bash
git clone https://github.com/nedozrel/places_remember.git
```

2. Move to the repository directory.

```bash
cd places_remember/
```

3. Create a virtual environment for the project (optional).

```bash
virtualenv env
source env/bin/activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Move to the Django project directory.

```bash
cd places_remember/
```

6. Create a `.env` file.

```bash
cp .env.example .env
```

7. In the `.env` file, fill in the environmental variables with the necessary values.

8. Move back to the project root directory.

```bash
cd ..
```

9. Create database.

```bash
python manage.py migrate
```

10. Start the server.

```bash
python manage.py runserver
```

11. Open http://127.0.0.1:8000 in your browser to see the index page.

### Using Docker Compose

1. Clone the repository.

```bash
git clone https://github.com/nedozrel/places_remember.git
```

2. Move to the repository directory.

```bash
cd places_remember/
```

3. Create a copy of the example environment file named `.env.example`.

```bash
cp .env.example .env
```

4. In the `.env` file, fill in the environmental variables with the necessary values.

5. Start the Docker Compose containers.

```bash
docker-compose up --build
```

6. Open http://localhost:8000 in your browser to access the index page.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
