import shlex
from typing import Any, Dict, List, Tuple

from const import COLORS


def print_welcome() -> None:
    print(f"{COLORS['cyan']}=== Todo List CLI ==={COLORS['reset']}")
    print("Type 'help' to see commands, 'exit' to quit.")


def print_help() -> None:
    help_text = """
Commands:
  project list
  project create <name> [description]
  project delete <name|id>
  
  task list [project_name]
  task add <project_name> <title> [tag1,tag2,...]
  task toggle <title|id>
  task delete <title|id>

  tag list
  tag create <name> [color]
  tag delete <name>

  exit
"""
    print(help_text)


def read_command() -> Tuple[str, List[str]]:
    """Reads input from user and parses it into command + args."""
    try:
        user_input = input(f"{COLORS['green']}todo>{COLORS['reset']} ").strip()
        if not user_input:
            return "", []
        parts = shlex.split(user_input)
        return parts[0].lower(), parts[1:]
    except ValueError as e:
        print(f"{COLORS['red']}Error parsing command: {e}{COLORS['reset']}")
        return "", []
    except KeyboardInterrupt:
        return "exit", []


def print_error(msg: str) -> None:
    print(f"{COLORS['red']}Error: {msg}{COLORS['reset']}")


def print_success(msg: str) -> None:
    print(f"{COLORS['green']}{msg}{COLORS['reset']}")


def print_projects(data: Dict[str, Any]) -> None:
    print(f"\n{COLORS['blue']}Projects:{COLORS['reset']}")
    if not data["projects"]:
        print("  (No projects)")
        return

    for p in data["projects"].values():
        print(f"  • {p['name']} (ID: {p['id']})")
        if p["description"]:
            print(f"    Desc: {p['description']}")


def print_tags(data: Dict[str, Any]) -> None:
    print(f"\n{COLORS['magenta']}Tags:{COLORS['reset']}")
    if not data["tags"]:
        print("  (No tags)")
        return

    for t in data["tags"].values():
        c_code = COLORS.get(t["color"], COLORS["white"])
        print(f"  • {c_code}#{t['name']}{COLORS['reset']} (ID: {t['id']})")


def print_tasks(data: Dict[str, Any], project_filter: str = None) -> None:
    print(f"\n{COLORS['yellow']}Tasks:{COLORS['reset']}")
    
    tasks = list(data["tasks"].values())
    if project_filter:
        # Find project id
        pid = None
        for p in data["projects"].values():
            if p["name"] == project_filter:
                pid = p["id"]
                break
        if pid:
            tasks = [t for t in tasks if t["project_id"] == pid]
        else:
            print(f"  (Project '{project_filter}' not found)")
            return

    if not tasks:
        print("  (No tasks)")
        return

    for t in tasks:
        symbol = "✅" if t["completed"] else "⭕"
        
        # Resolve project name
        p_name = "Unknown"
        if t["project_id"] in data["projects"]:
            p_name = data["projects"][t["project_id"]]["name"]

        # Resolve tags
        tag_str = ""
        for tid in t["tag_ids"]:
            if tid in data["tags"]:
                tag = data["tags"][tid]
                c = COLORS.get(tag["color"], COLORS["white"])
                tag_str += f" {c}#{tag['name']}{COLORS['reset']}"
        
        print(f"  {symbol} {t['title']} (Proj: {p_name}){tag_str}")