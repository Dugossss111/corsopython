# AGENTS.md - Development Guidelines for TodoList OOP

This document provides essential guidelines for agents working on the TodoList OOP project, focusing on build/lint/test commands and code style conventions.

## Project Overview

TodoList OOP is a command-line Python application for managing projects and tasks with a hierarchical structure using UUID-based identification and CLI interface.

## Build and Run Commands

### Running the Application
```bash
# Activate virtual environment
source venv/bin/activate

# Run the main application
python main.py
```

### Virtual Environment Management
```bash
# Create virtual environment (if not exists)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

## Testing Framework

**Current Status**: No testing framework is currently configured.

### Recommended Testing Setup
```bash
# Install pytest and testing dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run a specific test file
pytest tests/test_todolist.py

# Run a single test function (IMPORTANT for debugging)
pytest tests/test_todolist.py::TestTodolist::test_add_project

# Run tests in verbose mode
pytest -v
```

### Test Structure Guidelines
- Create `tests/` directory in project root
- Use `test_*.py` naming convention for test files
- Use `Test*` class naming for test classes

## Linting and Code Quality

**Current Status**: No linting tools are currently installed.

### Recommended Linting Setup
```bash
# Install linting and formatting tools
pip install pylint flake8 black isort mypy

# Run all linting checks
pylint *.py && flake8 *.py && mypy *.py

# Auto-format code
black *.py && isort *.py
```



## Code Style Guidelines

### Naming Conventions
- **Classes**: `PascalCase` (e.g., `Todolist`, `Project`, `Task`)
- **Methods**: `snake_case` (e.g., `add_project`, `get_tasks_length`)
- **Variables**: `snake_case` (e.g., `project_name`, `task_list`)
- **Constants**: `UPPER_SNAKE_CASE` (if any)
- **Private attributes**: Prefix with single underscore (e.g., `_internal_attr`)

### Import Organization
```python
# Standard library imports first
import uuid
from typing import List, Optional

# Local imports
from project import Project
from task import Task
```

### Class Structure
```python
class ClassName:
    def __init__(self, param: Type) -> None:
        """Initialize class with parameters."""
        self.param = param

    def public_method(self, param: Type) -> ReturnType:
        """Public method description."""
        pass
```

### Docstrings
```python
def method_name(self, param: Type) -> ReturnType:
    """One-line summary of what the method does.

    Args:
        param: Description of parameter

    Returns:
        Description of return value
    """
```



## Error Handling

### Exception Types
- **`ValueError`**: Invalid input values (empty strings, invalid formats)
- **`TypeError`**: Wrong parameter types
- **`IndexError`**: Accessing non-existent list indices
- **`KeyError`**: Accessing non-existent dictionary keys

### Error Handling Patterns
- Use `ValueError` for invalid input values (empty strings, invalid formats)
- Use `TypeError` for wrong parameter types
- Validate inputs at method boundaries





---

## Quick Reference

### Most Common Commands
```bash
# Run application
./venv/bin/python main.py

# Format code
black *.py && isort *.py

# Check quality
pylint *.py && mypy *.py

# Run tests (when available)
pytest
```