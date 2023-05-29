import sqlite3
from pathlib import Path


db_path = Path(__file__) / "db.sqlite3"
connector = sqlite3.connect(db_path)
cursor = connector.cursor()


def default():

    with open("game_data/tables.sql") as file:
        schemas = file.read()
        schemas = schemas.split("\n\n")
    for schema in schemas:
        cursor.execute(schema)
        connector.commit()
    add_settings()


def add_settings():
    cursor.execute("SELECT * FROM settings;")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO settings VALUES (?, ?, ?);", (1, 1, 50))
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
