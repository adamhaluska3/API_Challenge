# ApiChallenge
This project features a RESTful API for creating, editing, and retrieving data about different countries. It is built using [Django REST framework](https://www.django-rest-framework.org/) and uses SQLite as a database.

## Features
Users can:
- Retrieve information about multiple countries with pagination available,
- Retrieve information about a specific country based on the ID provided,
- Edit existing countries' names and country codes,
- Create new countries.

## Prerequisites
- Python (3.10+)

## Installation
- Clone [this repository](https://github.com/adamhaluska3/API_Challenge).
- Create and activate virtual environment (venv):
    - Windows: 
    ```
    python -m venv /path/to/venv
    ./path/to/venv/Script/activate
    ```
    - Linux:
    ```
    python -m venv /path/to/venv
    source ./path/to/venv/bin/activate
    ```
- Install dependencies from **requirements.txt**:
    ```
    pip install -r /path/to/requirements.txt
    ```
- Set up database:
    ```
    python manage.py migrate
    ```
- Launch API server:
    ```
    python manage.py runserver ('0.0.0.0:<wanted_port>' for public server at wanted port [requires port forwarding])
    ```

## API Endpoints
| HTTP Method | Endpoint | Action |
| --- | --- | --- |
| GET | /countries/\<id> | Retrieves country with given ID (if exists). |
| PUT | /countries/\<id> | Updates existing country's name and country code. |
| GET | /countries | Retrieves a list of countries; filter by _*CountryCodeFiltr*_, _*PageLimit*_ and _*PageOffset*_ pagination available via URL parameters. |
| POST | /countries | Creates new country with given name and country code. |

## Author
- Adam Haluška <adam.haluska3@gmail.com>
