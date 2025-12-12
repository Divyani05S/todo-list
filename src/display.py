"""
Display utilities for formatting todo list output.
"""

from typing import List, Dict


def format_todo(todo: Dict, detailed: bool = False) -> str:
    """
    Format a single todo item for display.
    
    Args:
        todo: Todo dictionary
        detailed: Whether to show detailed information
        
    Returns:
        Formatted string
    """
    status = "[X]" if todo['completed'] else "[ ]"
    todo_id = todo['id']
    title = todo['title']
    priority = todo.get('priority', 'medium')  # NEW PRIORITY FIELD
    
    if detailed:
        description = f"\n   Description: {todo['description']}" if todo['description'] else ""
        created = f"\n   Created: {todo['created_at']}"
        completed = f"\n   Completed: {todo['completed_at']}" if todo['completed'] else ""
        return (
            f"{status} ID: {todo_id} - {title} (Priority: {priority})"
            f"{description}{created}{completed}"
        )
    else:
        return f"{status} ID: {todo_id} - {title} (Priority: {priority})"  # UPDATED


def display_todos(todos: List[Dict], detailed: bool = False) -> None:
    """
    Display a list of todos.
    
    Args:
        todos: List of todo dictionaries
        detailed: Whether to show detailed information
    """
    if not todos:
        print("\nNo todos found.")
        return
    
    print("\n" + "=" * 60)
    print("                    TODO LIST")
    print("=" * 60)
    
    for todo in todos:
        print(format_todo(todo, detailed))
    
    print("=" * 60)


def display_stats(stats: Dict) -> None:
    """
    Display todo statistics.
    
    Args:
        stats: Statistics dictionary
    """
    print("\n" + "=" * 60)
    print("                    STATISTICS")
    print("=" * 60)
    print(f"Total Todos: {stats['total']}")
    print(f"Completed: {stats['completed']}")
    print(f"Pending: {stats['pending']}")
    print(f"Completion Rate: {stats['completion_rate']}%")
    print("=" * 60)


def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("                    TODO LIST MANAGER")
    print("=" * 60)
    print("1. Add a new todo")
    print("2. List all todos")
    print("3. List pending todos")
    print("4. Mark todo as completed")
    print("5. Mark todo as pending")
    print("6. Update todo")
    print("7. Delete todo")
    print("8. View statistics")
    print("9. Exit")
    print("=" * 60)
