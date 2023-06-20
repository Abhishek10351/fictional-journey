import json
import sqlite3
from pathlib import Path

folder_path = Path(__file__).parent
db_path = folder_path / "db.sqlite3"
schema_path = folder_path / "tables.sql"
powerups_path = folder_path / "powerups.json"
levels_path = folder_path / "levels.json"
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
    add_levels()


def add_settings():
    if not fetch("SELECT * FROM settings;"):
        execute("INSERT INTO settings VALUES (?, ?, ?);", 1, 1, 50)


def add_levels():
    with open(levels_path, 'r') as json_file:
        levels = json.load(json_file)["levels"]

    for level in levels:
        if not fetch("SELECT * FROM levels WHERE level = ?", level["level"]):
            execute('''INSERT INTO levels ( level, name, description, 
            objective ) VALUES (?, ?, ?, ?)''',
                    level["level"], level["name"], level["description"],
                    level["objective"])
        execute("UPDATE levels SET completed = 1 WHERE level = 1")


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
