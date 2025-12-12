"""
Todo Manager - Handles all todo list operations.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class TodoManager:
    """Manages todo items with persistence to JSON file."""
    
    def __init__(self, data_file: str = "todos.json"):
        """
        Initialize the TodoManager.
        
        Args:
            data_file: Path to the JSON file for storing todos
        """
        self.data_file = data_file
        self.todos = self._load_todos()
    
    def _load_todos(self) -> List[Dict]:
        """
        Load todos from JSON file.
        
        Returns:
            List of todo dictionaries
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_todos(self) -> bool:
        """
        Save todos to JSON file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, indent=2, ensure_ascii=False)
            return True
        except IOError:
            return False
    
    def add_todo(self, title: str, description: str = "") -> Dict:
        """
        Add a new todo item.
        
        Args:
            title: Todo title (required)
            description: Todo description (optional)
            
        Returns:
            Dictionary with the created todo item
        """
        if not title.strip():
            raise ValueError("Todo title cannot be empty.")
        
        todo = {
            'id': len(self.todos) + 1,
            'title': title.strip(),
            'description': description.strip(),
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'completed_at': None
        }
        
        self.todos.append(todo)
        self._save_todos()
        return todo
    
    def list_todos(self, show_completed: bool = True) -> List[Dict]:
        """
        Get all todos, optionally filtering completed ones.
        
        Args:
            show_completed: Whether to include completed todos
            
        Returns:
            List of todo dictionaries
        """
        if show_completed:
            return self.todos
        return [todo for todo in self.todos if not todo['completed']]
    
    def get_todo(self, todo_id: int) -> Optional[Dict]:
        """
        Get a specific todo by ID.
        
        Args:
            todo_id: ID of the todo item
            
        Returns:
            Todo dictionary if found, None otherwise
        """
        for todo in self.todos:
            if todo['id'] == todo_id:
                return todo
        return None
    
    def complete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as completed.
        
        Args:
            todo_id: ID of the todo item
            
        Returns:
            True if successful, False if todo not found
        """
        todo = self.get_todo(todo_id)
        if todo:
            todo['completed'] = True
            todo['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._save_todos()
            return True
        return False
    
    def uncomplete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as not completed.
        
        Args:
            todo_id: ID of the todo item
            
        Returns:
            True if successful, False if todo not found
        """
        todo = self.get_todo(todo_id)
        if todo:
            todo['completed'] = False
            todo['completed_at'] = None
            self._save_todos()
            return True
        return False
    
    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item.
        
        Args:
            todo_id: ID of the todo item
            
        Returns:
            True if successful, False if todo not found
        """
        todo = self.get_todo(todo_id)
        if todo:
            self.todos.remove(todo)
            # Reassign IDs to maintain sequential order
            for i, t in enumerate(self.todos, 1):
                t['id'] = i
            self._save_todos()
            return True
        return False
    
    def update_todo(self, todo_id: int, title: str = None, description: str = None) -> bool:
        """
        Update a todo item's title and/or description.
        
        Args:
            todo_id: ID of the todo item
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            True if successful, False if todo not found
        """
        todo = self.get_todo(todo_id)
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
        
        Returns:
            Dictionary with todo statistics
        """
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo['completed'])
        pending = total - completed
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'completion_rate': round((completed / total * 100) if total > 0 else 0, 1)
        }
