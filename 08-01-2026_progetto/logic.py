import datetime
import uuid
from typing import Any, Dict, List, Optional


# --- Helper Functions ---

def generate_uuid() -> str:
    """Generates a unique string ID."""
    return str(uuid.uuid4())


def get_timestamp() -> str:
    """Returns current ISO format timestamp."""
    return datetime.datetime.now().isoformat()


# --- Projects ---

def create_project(data: Dict[str, Any], name: str, description: str = "") -> bool:
    """Creates a new project. Returns True if successful, False if name exists."""
    # Check uniqueness
    for proj in data["projects"].values():
        if proj["name"] == name:
            return False

    pid = generate_uuid()
    data["projects"][pid] = {
        "id": pid,
        "name": name,
        "description": description,
        "created_at": get_timestamp()
    }
    return True


def delete_project(data: Dict[str, Any], project_name_or_id: str) -> bool:
    """Deletes a project and all its tasks by name or ID. Returns True if found."""
    # Resolve project ID
    pid_found = None
    if project_name_or_id in data["projects"]:
        pid_found = project_name_or_id
    else:
        for pid, proj in data["projects"].items():
            if proj["name"] == project_name_or_id:
                pid_found = pid
                break
    
    if not pid_found:
        return False
        
    # Delete tasks associated with this project
    tasks_to_delete = []
    for tid, task in data["tasks"].items():
        if task["project_id"] == pid_found:
            tasks_to_delete.append(tid)
            
    for tid in tasks_to_delete:
        del data["tasks"][tid]

    # Delete project
    del data["projects"][pid_found]
    return True


def get_project_by_name(data: Dict[str, Any], name: str) -> Optional[Dict[str, Any]]:
    for proj in data["projects"].values():
        if proj["name"] == name:
            return proj
    return None


# --- Tags ---

def create_tag(data: Dict[str, Any], name: str, color: str = "white") -> bool:
    """Creates a new tag. Returns True if successful, False if name exists."""
    for tag in data["tags"].values():
        if tag["name"] == name:
            return False

    tid = generate_uuid()
    data["tags"][tid] = {
        "id": tid,
        "name": name,
        "color": color
    }
    return True


def delete_tag(data: Dict[str, Any], tag_name: str) -> bool:
    """Deletes a tag. Removes it from all tasks."""
    tid_found = None
    for tid, tag in data["tags"].items():
        if tag["name"] == tag_name:
            tid_found = tid
            break
            
    if not tid_found:
        return False

    # Remove from tasks
    for task in data["tasks"].values():
        if tid_found in task["tag_ids"]:
            task["tag_ids"].remove(tid_found)

    del data["tags"][tid_found]
    return True


def get_tag_by_name(data: Dict[str, Any], name: str) -> Optional[Dict[str, Any]]:
    for tag in data["tags"].values():
        if tag["name"] == name:
            return tag
    return None


# --- Tasks ---

def add_task(data: Dict[str, Any], project_name: str, title: str, tag_names: List[str]) -> bool:
    """Adds a task to a project. Returns False if project not found."""
    project = get_project_by_name(data, project_name)
    if not project:
        return False

    # Check title uniqueness (globally as per strict reading, or per project?)
    # Implementation: Global title uniqueness requested in prompt? 
    # "Task ha: titolo (univoco)" -> Global seems implied or per project. 
    # Let's enforce global for safety based on the note.
    for t in data["tasks"].values():
        if t["title"] == title:
            return False

    # Resolve tags
    tag_ids = []
    for t_name in tag_names:
        tag = get_tag_by_name(data, t_name)
        if tag:
            tag_ids.append(tag["id"])

    tid = generate_uuid()
    data["tasks"][tid] = {
        "id": tid,
        "title": title,
        "completed": False,
        "project_id": project["id"],
        "tag_ids": tag_ids,
        "created_at": get_timestamp(),
        "completed_at": None
    }
    return True


def toggle_task(data: Dict[str, Any], title_or_id: str) -> bool:
    """Toggles task completion status."""
    task_found = _find_task(data, title_or_id)
    if not task_found:
        return False

    task_found["completed"] = not task_found["completed"]
    if task_found["completed"]:
        task_found["completed_at"] = get_timestamp()
    else:
        task_found["completed_at"] = None
        
    return True


def delete_task(data: Dict[str, Any], title_or_id: str) -> bool:
    """Deletes a task."""
    task_found = _find_task(data, title_or_id)
    if not task_found:
        return False
        
    del data["tasks"][task_found["id"]]
    return True


def _find_task(data: Dict[str, Any], identifier: str) -> Optional[Dict[str, Any]]:
    """Helper to find task by ID or Title."""
    if identifier in data["tasks"]:
        return data["tasks"][identifier]
    
    for task in data["tasks"].values():
        if task["title"] == identifier:
            return task
    return None