from typing import Dict

# File Paths
DB_DIR = "db"
DB_FILE = "db.json"

# ANSI Colors
COLORS: Dict[str, str] = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m",
}

# Default initial data structure
DEFAULT_DB_DATA = {
    "projects": {},
    "tags": {},
    "tasks": {}
}