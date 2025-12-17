"""
Todo List Manager - A simple CLI application for managing todos.

No external API keys required - everything runs locally!
"""

# this comment is for qodo test
# this comment is for self-hosted qodo test
# this comment is for self-hosted qodo test 2
# this comment is for self-hosted qodo test 3

import sys
import random  # <--- NEW IMPORT
from todo_manager import TodoManager
from display import display_todos, display_stats, display_menu


def get_user_input(prompt: str) -> str:
    """
    Get input from user with error handling.
    
    Args:
        prompt: Input prompt text
        
    Returns:
        User input string
    """
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting...")
        sys.exit(0)


def get_int_input(prompt: str) -> int:
    """
    Get integer input from user with validation.
    
    Args:
        prompt: Input prompt text
        
    Returns:
        Integer value
        
    Raises:
        ValueError: If input cannot be converted to integer
    """
    value = get_user_input(prompt)
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid input: '{value}'. Please enter a number.")


def add_todo_interactive(manager: TodoManager) -> None:
    """Interactive function to add a new todo."""
    print("\n--- Add New Todo ---")
    title = get_user_input("Enter todo title: ")
    
    if not title:
        print("[ERROR] Title cannot be empty.")
        return
    
    description = get_user_input("Enter description (optional, press Enter to skip): ")

    # NEW: Ask for priority
    priority = get_user_input("Enter priority (low/medium/high, default=medium): ").lower()
    if priority not in ["low", "medium", "high", ""]:
        print("[ERROR] Invalid priority. Allowed values: low, medium, high.")
        return

    if priority == "":
        priority = "medium"

    try:
        todo = manager.add_todo(title, description)

        # NEW: Store priority after creation
        todo["priority"] = priority
        manager._save_todos()

        print(f"\n[SUCCESS] Todo added successfully!")
        print(f"  ID: {todo['id']} - {todo['title']} (Priority: {todo['priority']})")
    except ValueError as e:
        print(f"[ERROR] {e}")


def list_todos_interactive(manager: TodoManager, show_completed: bool = True) -> None:
    """Interactive function to list todos."""
    todos = manager.list_todos(show_completed=show_completed)
    display_todos(todos, detailed=False)


def complete_todo_interactive(manager: TodoManager) -> None:
    """Interactive function to mark a todo as completed."""
    print("\n--- Complete Todo ---")
    try:
        todo_id = get_int_input("Enter todo ID to mark as completed: ")
        if manager.complete_todo(todo_id):
            print(f"[SUCCESS] Todo {todo_id} marked as completed!")
        else:
            print(f"[ERROR] Todo with ID {todo_id} not found.")
    except ValueError as e:
        print(f"[ERROR] {e}")


def uncomplete_todo_interactive(manager: TodoManager) -> None:
    """Interactive function to mark a todo as pending."""
    print("\n--- Mark Todo as Pending ---")
    try:
        todo_id = get_int_input("Enter todo ID to mark as pending: ")
        if manager.uncomplete_todo(todo_id):
            print(f"[SUCCESS] Todo {todo_id} marked as pending!")
        else:
            print(f"[ERROR] Todo with ID {todo_id} not found.")
    except ValueError as e:
        print(f"[ERROR] {e}")


def update_todo_interactive(manager: TodoManager) -> None:
    """Interactive function to update a todo."""
    print("\n--- Update Todo ---")
    try:
        todo_id = get_int_input("Enter todo ID to update: ")
        todo = manager.get_todo(todo_id)
        
        if not todo:
            print(f"[ERROR] Todo with ID {todo_id} not found.")
            return
        
        print(f"Current title: {todo['title']}")
        new_title = get_user_input("Enter new title (press Enter to keep current): ")
        
        print(f"Current description: {todo['description']}")
        new_description = get_user_input("Enter new description (press Enter to keep current): ")

        # NEW: Priority update support
        print(f"Current priority: {todo.get('priority', 'medium')}")
        new_priority = get_user_input("Enter new priority (low/medium/high, press Enter to keep current): ").lower()

        if new_priority not in ["low", "medium", "high", ""]:
            print("[ERROR] Invalid priority. Allowed: low, medium, high.")
            return
        
        priority = new_priority if new_priority else todo.get("priority", "medium")

        title = new_title if new_title else None
        description = new_description if new_description else None
        
        if manager.update_todo(todo_id, title, description):
            # Save updated priority
            todo["priority"] = priority
            manager._save_todos()
            print(f"[SUCCESS] Todo {todo_id} updated successfully!")
        else:
            print(f"[ERROR] Failed to update todo {todo_id}.")
    except ValueError as e:
        print(f"[ERROR] {e}")


def delete_todo_interactive(manager: TodoManager) -> None:
    """Interactive function to delete a todo."""
    print("\n--- Delete Todo ---")
    try:
        todo_id = get_int_input("Enter todo ID to delete: ")
        todo = manager.get_todo(todo_id)
        
        if not todo:
            print(f"[ERROR] Todo with ID {todo_id} not found.")
            return
        
        confirm = get_user_input(f"Are you sure you want to delete '{todo['title']}'? (yes/no): ")
        
        if confirm.lower() in ['yes', 'y']:
            if manager.delete_todo(todo_id):
                print(f"[SUCCESS] Todo {todo_id} deleted successfully!")
            else:
                print(f"[ERROR] Failed to delete todo {todo_id}.")
        else:
            print("Deletion cancelled.")
    except ValueError as e:
        print(f"[ERROR] {e}")


def view_stats_interactive(manager: TodoManager) -> None:
    """Interactive function to view statistics."""
    stats = manager.get_stats()
    display_stats(stats)
    
    # --- NEW FEATURE: MOTIVATIONAL QUOTES ---
    quotes = [
        "Small steps lead to big changes.",
        "Action is the foundational key to all success.",
        "Don't count the days, make the days count.",
        "The secret of getting ahead is getting started.",
        "Well done is better than well said."
    ]
    print(f"\n💡 Daily Motivation: {random.choice(quotes)}")
    # ----------------------------------------


def main():
    """Main function to run the todo list manager."""
    manager = TodoManager()
    
    print("\n" + "=" * 60)
    print("          Welcome to Todo List Manager!")
    print("=" * 60)
    print("Your todos are saved locally in 'todos.json'")
    
    while True:
        display_menu()
        choice = get_user_input("\nEnter your choice (1-9): ")
        
        if choice == '1':
            add_todo_interactive(manager)
        elif choice == '2':
            list_todos_interactive(manager, show_completed=True)
        elif choice == '3':
            list_todos_interactive(manager, show_completed=False)
        elif choice == '4':
            complete_todo_interactive(manager)
        elif choice == '5':
            uncomplete_todo_interactive(manager)
        elif choice == '6':
            update_todo_interactive(manager)
        elif choice == '7':
            delete_todo_interactive(manager)
        elif choice == '8':
            view_stats_interactive(manager)
        elif choice == '9':
            print("\nThank you for using Todo List Manager!")
            print("Your todos have been saved.")
            break
        else:
            print("[ERROR] Invalid choice. Please enter a number between 1 and 9.")
        
        # Pause before showing menu again
        if choice != '9':
            get_user_input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
