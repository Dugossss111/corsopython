import json
import os
from typing import Any, Dict

from const import DB_DIR, DB_FILE, DEFAULT_DB_DATA


def get_db_path() -> str:
    """Returns the absolute path to the database file."""
    return os.path.join(os.getcwd(), DB_DIR, DB_FILE)


def load_db() -> Dict[str, Any]:
    """
    Loads the database from the JSON file.
    If the file or directory does not exist, it creates them.
    """
    db_path = get_db_path()

    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    if not os.path.exists(db_path):
        save_db(DEFAULT_DB_DATA)
        return DEFAULT_DB_DATA

    try:
        with open(db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Ensure all keys exist even if file was partial
            for key in DEFAULT_DB_DATA:
                if key not in data:
                    data[key] = {}
            return data
    except (json.JSONDecodeError, IOError):
        # If corrupt, backup? For now, imply return default or fail.
        # Let's return default but maybe warn in real app.
        return DEFAULT_DB_DATA


def save_db(data: Dict[str, Any]) -> None:
    """Saves the data dictionary to the JSON file."""
    db_path = get_db_path()
    
    # Ensure dir exists before saving (just in case deleted runtime)
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)