# Django Crossing

An app to catalog villagers, the diys you recieve from them, and critters from Animal Crossing: New Horizons! Created using Python, Django, Postgres.

## Routes Table

| Verb   | Path                      | Action             |
|--------|---------------------------|--------------------|
| GET    | `characters/villagers/`   | `index`            |
| GET    | `characters/villagers/:pk`| `show`             |
| POST   | `characters/villagers/`   | `create`           |
| PATCH  | `characters/villagers/:pk`| `update`           |
| DELETE | `characters/villagers/:pk`| `destroy`          |
| GET    | `characters/diys/`        | `index`            |
| GET    | `characters/diys/:pk`     | `show`             |
| POST   | `characters/diys/`        | `create`           |
| PATCH  | `characters/diys/:pk`     | `update`           |
| DELETE | `characters/diys/:pk`     | `destroy`          |

| Verb   | Path            | Action             |
|--------|-----------------|--------------------|
| GET    | `/bugs/`        | `index`            |
| GET    | `/bugs/:pk`     | `show`             |
| POST   | `/bugs/`        | `create`           |
| PATCH  | `/bugs/`        | `update`           |
| DELETE | `/bugs/:pk`     | `destroy`          |

## Starting Instructions

Install dependencies:

`pip3 install --upgrade pip`

`pip install pipenv`

`pipenv install django==4.1 psycopg2-binary`

`python manage.py runserver`