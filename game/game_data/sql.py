import sqlite3
connector = sqlite3.connect("game_data/db.sqlite3")
cursor = connector.cursor()


def default():

    with open("game_data/tables.sql") as file:
        schemas = file.read()
        schemas = schemas.split("\n\n")
    for schema in schemas:
        cursor.execute(schema)
        connector.commit()


default()


def execute(query, *parameters):
    cursor.execute(query, parameters)
    connector.commit()


def fetch(query, *parameters):
    cursor.execute(query, parameters)
    return cursor.fetchone()


def fetchall(query, *parameters):
    cursor.execute(query, parameters)
    return cursor.fetchall()
