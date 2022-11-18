# Django Crossing

An app to catalog villagers and critters from Animal Crossing: New Horizons. Created using Python, Django, Postgres.

## Routes Table

| /villagers/    | GET    | index    | Show all villagers      |
| :---:          | :---:  | :---:    | :---:                   |
| /bugs/         | GET    | index    | Show all bugs           |
| :---:          | :---:  | :---:    | :---:                   |
| /villagers/    | POST   | create   | Create a villager       |
| :---:          | :---:  | :---:    | :---:                   |
| /bugs/         | POST   | create   | Create a bug            |
| :---:          | :---:  | :---:    | :---:                   |
| /villagers/:pk | GET    | show     | Show villager with pk   |
| :---:          | :---:  | :---:    | :---:                   |
| /bugs/:pk      | GET    | show     | Show bug with pk        |
| :---:          | :---:  | :---:    | :---:                   |
| /villagers/:pk | PATCH  | update   | Update villager with pk |
| :---:          | :---:  | :---:    | :---:                   |
| /bugs/:pk      | PATCH  | update   | Update bug with pk      |
| :---:          | :---:  | :---:    | :---:                   |
| /villagers/:pk | DELETE | destroy  | Delete villager with pk |
| :---:          | :---:  | :---:    | :---:                   |
| /bugs/:pk      | DELETE | destroy  | Delete bug with pk      |

## Starting Instructions

`pip3 install --upgrade pip`
`pip install pipenv`
`pipenv shell`
`pipenv install django==4.1 psycopg2-binary`
`python manage.py runserver`