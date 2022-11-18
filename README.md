# Django Crossing

An app to catalog villagers and critters from Animal Crossing: New Horizons. Created using Python, Django, Postgres.

## Routes Table

| Verb   | Path            | Action             |
|--------|-----------------|--------------------|
| GET    | `/villagers/`   | `index`            |
| GET    | `/villagers/:pk`| `show`             |
| POST   | `/villagers/`   | `create`           |
| PATCH  | `/villagers/`   | `update`           |
| DELETE | `/villagers/:pk`| `destroy`          |

| Verb   | Path            | Action             |
|--------|-----------------|--------------------|
| GET    | `/bugs/`        | `index`            |
| GET    | `/bugs/:pk`     | `show`             |
| POST   | `/bugs/`        | `create`           |
| PATCH  | `/bugs/`        | `update`           |
| DELETE | `/bugs/:pk`     | `destroy`          |

## Starting Instructions

`pip3 install --upgrade pip`

`pip install pipenv`

`pipenv shell`

`pipenv install django==4.1 psycopg2-binary`

`python manage.py runserver`