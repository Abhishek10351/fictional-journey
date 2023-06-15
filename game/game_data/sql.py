import json
import sqlite3
from pathlib import Path

folder_path = Path(__file__).parent
db_path = folder_path / "db.sqlite3"
schema_path = folder_path / "tables.sql"
powerups_path = folder_path / "powerups.json"
connector = sqlite3.connect(db_path)
cursor = connector.cursor()


def default():

    with open(schema_path) as file:
        schemas = file.read()
        schemas = schemas.split("\n\n")
    for schema in schemas:
        cursor.execute(schema)
        connector.commit()
    add_settings()
    add_powerups()


def add_settings():
    if not fetch("SELECT * FROM settings;"):
        execute("INSERT INTO settings VALUES (?, ?, ?);", (1, 1, 50))


def add_powerups():
    with open(powerups_path, 'r') as json_file:
        powerups = json.load(json_file)["powerups"]

    for powerup in powerups:
        if not fetch("SELECT * FROM powerups WHERE id = ?", powerup["id"]):
            execute('''INSERT INTO powerups
                            VALUES (?, ?, ?, ?, ?, ?)''',
                    powerup["id"], powerup["name"], powerup["description"],
                    powerup["duration"], powerup["rarity"], powerup["asset_path"])


def execute(query, *parameters):
    cursor.execute(query, parameters)
    connector.commit()


def fetch(query, *parameters):
    cursor.execute(query, parameters)
    return cursor.fetchone()


def fetchall(query, *parameters):
    cursor.execute(query, parameters)
    return cursor.fetchall()


default()
