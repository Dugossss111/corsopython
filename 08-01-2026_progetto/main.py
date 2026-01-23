import sys
from typing import List

from data import load_db, save_db
import logic
import ui


def handle_project_command(data, args: List[str]) -> None:
    if not args:
        ui.print_error("Missing subcommand for project")
        return

    sub = args[0]
    if sub == "list":
        ui.print_projects(data)
    elif sub == "create":
        if len(args) < 2:
            ui.print_error("Usage: project create <name> [desc]")
            return
        name = args[1]
        desc = args[2] if len(args) > 2 else ""
        if logic.create_project(data, name, desc):
            ui.print_success(f"Project '{name}' created.")
            save_db(data)
        else:
            ui.print_error(f"Project '{name}' already exists.")
    elif sub == "delete":
        if len(args) < 2:
            ui.print_error("Usage: project delete <name|id>")
            return
        if logic.delete_project(data, args[1]):
            ui.print_success(f"Project '{args[1]}' deleted.")
            save_db(data)
        else:
            ui.print_error(f"Project '{args[1]}' not found.")
    else:
        ui.print_error(f"Unknown project command: {sub}")


def handle_tag_command(data, args: List[str]) -> None:
    if not args:
        ui.print_error("Missing subcommand for tag")
        return
    
    sub = args[0]
    if sub == "list":
        ui.print_tags(data)
    elif sub == "create":
        if len(args) < 2:
            ui.print_error("Usage: tag create <name> [color]")
            return
        name = args[1]
        color = args[2] if len(args) > 2 else "white"
        if logic.create_tag(data, name, color):
            ui.print_success(f"Tag '{name}' created.")
            save_db(data)
        else:
            ui.print_error(f"Tag '{name}' already exists.")
    elif sub == "delete":
        if len(args) < 2:
            ui.print_error("Usage: tag delete <name>")
            return
        if logic.delete_tag(data, args[1]):
            ui.print_success(f"Tag '{args[1]}' deleted.")
            save_db(data)
        else:
            ui.print_error(f"Tag '{args[1]}' not found.")
    else:
        ui.print_error(f"Unknown tag command: {sub}")


def handle_task_command(data, args: List[str]) -> None:
    if not args:
        ui.print_error("Missing subcommand for task")
        return

    sub = args[0]
    if sub == "list":
        project_filter = args[1] if len(args) > 1 else None
        ui.print_tasks(data, project_filter)
    elif sub == "add":
        # task add <project> <title> [tag1,tag2]
        if len(args) < 3:
            ui.print_error("Usage: task add <project> <title> [tags]")
            return
        proj = args[1]
        title = args[2]
        tags = args[3].split(",") if len(args) > 3 else []
        if logic.add_task(data, proj, title, tags):
            ui.print_success(f"Task '{title}' added.")
            save_db(data)
        else:
            ui.print_error("Could not add task. Check if project exists or title is unique.")
    elif sub == "toggle":
        if len(args) < 2:
            ui.print_error("Usage: task toggle <title|id>")
            return
        if logic.toggle_task(data, args[1]):
            ui.print_success(f"Task '{args[1]}' toggled.")
            save_db(data)
        else:
            ui.print_error(f"Task '{args[1]}' not found.")
    elif sub == "delete":
        if len(args) < 2:
            ui.print_error("Usage: task delete <title|id>")
            return
        if logic.delete_task(data, args[1]):
            ui.print_success(f"Task '{args[1]}' deleted.")
            save_db(data)
        else:
            ui.print_error(f"Task '{args[1]}' not found.")
    else:
        ui.print_error(f"Unknown task command: {sub}")


def main() -> None:
    data = load_db()
    
    ui.print_welcome()
    
    while True:
        cmd, args = ui.read_command()
        
        if cmd == "exit":
            print("Bye!")
            break
        elif cmd == "help":
            ui.print_help()
        elif cmd == "project":
            handle_project_command(data, args)
        elif cmd == "tag":
            handle_tag_command(data, args)
        elif cmd == "task":
            handle_task_command(data, args)
        elif cmd == "":
            continue
        else:
            ui.print_error(f"Unknown command: {cmd}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)