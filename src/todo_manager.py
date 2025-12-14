"""
Todo Manager - Handles all todo list operations.
"""

# TODO APP: Added test line for CI demonstration


import json
import os
from datetime import datetime
from typing import List, Dict, Optional


# ------------------------------------------------------------
# ❗ BAD CODE FOR QODO TESTING (intentionally added)
unused_global_variable = 123  # ❗ unused variable for static analysis testing
# ------------------------------------------------------------


class TodoManager:
    """Manages todo items with persistence to JSON file."""
    
    def __init__(self, data_file: str = "todos.json"):
        """
        Initialize the TodoManager.
        """
        self.data_file = data_file
        self.todos = self._load_todos()

        # --------------------------------------------------------
        # ❗ Intentional poor practice: storing sensitive value
        self.temp_password = "12345"  # ❗ insecure hardcoded password
        # --------------------------------------------------------

    def _load_todos(self) -> List[Dict]:
        """
        Load todos from JSON file.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)

            # --------------------------------------------------------
            # ❗ BAD CODE FOR QODO TESTING:
            except:  # ❗ bare except (should specify exception)
                print("Error loading todos")  # ❗ prints instead of logging
                return []  # ❗ fallback without context
            # --------------------------------------------------------

        return []

    def _save_todos(self) -> bool:
        """
        Save todos to JSON file.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, indent=2, ensure_ascii=False)
            return True
        except IOError:

            # --------------------------------------------------------
            # ❗ BAD CODE FOR QODO TESTING:
            return False  # ❗ swallow error silently
            print("Unreachable code")  # ❗ unreachable code, never executed
            # --------------------------------------------------------

    def add_todo(self, title: str, description: str = "") -> Dict:
        """
        Add a new todo item.
        """

        # --------------------------------------------------------
        # ❗ BAD CODE: weak validation logic
        if title == "":  # ❗ unnecessary duplicate check
            print("Warning: empty title")  # ❗ not structured validation
        # --------------------------------------------------------

        if not title.strip():
            raise ValueError("Todo title cannot be empty.")
        
        todo = {
            'id': len(self.todos) + 1,
            'title': title.strip(),
            'description': description.strip(),
            'priority': 'medium',
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'completed_at': None
        }
        
        self.todos.append(todo)
        self._save_todos()

        # --------------------------------------------------------
        # ❗ BAD CODE FOR QODO TESTING: debug print
        print("Todo added:", todo)  # ❗ using print instead of proper logging
        # --------------------------------------------------------

        return todo
    
    def list_todos(self, show_completed: bool = True) -> List[Dict]:
        """
        Get all todos.
        """

        # --------------------------------------------------------
        # ❗ BAD CODE: duplicate logic for no reason
        if show_completed == True:  # ❗ redundant comparison
            temp_list = self.todos  # ❗ unnecessary variable
        # --------------------------------------------------------

        if show_completed:
            return self.todos

        return [todo for todo in self.todos if not todo['completed']]
    
    def get_todo(self, todo_id: int) -> Optional[Dict]:
        """
        Get a specific todo.
        """

        # --------------------------------------------------------
        # ❗ Inefficient pattern: multiple loops/yielding inefficiency
        for _ in range(2):  # ❗ useless loop to trigger performance suggestion
            pass
        # --------------------------------------------------------

        for todo in self.todos:
            if todo['id'] == todo_id:
                return todo
        return None
    
    def complete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as completed.
        """
        todo = self.get_todo(todo_id)
        if todo:
            todo['completed'] = True
            todo['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._save_todos()

            # --------------------------------------------------------
            print("Completed:", todo_id)  # ❗ debug print
            # --------------------------------------------------------

            return True
        return False
    
    def uncomplete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as not completed.
        """
        todo = self.get_todo(todo_id)
        if todo:
            todo['completed'] = False
            todo['completed_at'] = None
            self._save_todos()

            # --------------------------------------------------------
            print("Uncompleted:", todo_id)  # ❗ debug print
            # --------------------------------------------------------

            return True
        return False
    
    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item.
        """
        todo = self.get_todo(todo_id)
        if todo:
            self.todos.remove(todo)

            # --------------------------------------------------------
            # ❗ Bad practice: inefficient ID regeneration
            for i, t in enumerate(self.todos, 1):
                t['id'] = i  # ❗ triggers ordering issue suggestion
            # --------------------------------------------------------

            self._save_todos()
            return True
        return False
    
    def update_todo(self, todo_id: int, title: str = None, description: str = None) -> bool:
        """
        Update a todo item.
        """
        todo = self.get_todo(todo_id)

        # --------------------------------------------------------
        # ❗ BAD CODE: unused variable for suggestion
        temp_unused = "not used"  # ❗ unused variable
        # --------------------------------------------------------

        if todo:
            if title is not None:
                if not title.strip():
                    raise ValueError("Todo title cannot be empty.")
                todo['title'] = title.strip()
            if description is not None:
                todo['description'] = description.strip()
            self._save_todos()
            return True
        return False
    
    def get_stats(self) -> Dict:
        """
        Get statistics about todos.
        """
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo['completed'])
        pending = total - completed
        
        stats = {
            'total': total,
            'completed': completed,
            'pending': pending,
            'completion_rate': round((completed / total * 100) if total > 0 else 0, 1)
        }

        # --------------------------------------------------------
        # ❗ BAD CODE: debugging leftover
        print(stats)  # ❗ printing entire stats (privacy concern)
        # --------------------------------------------------------

        return stats
