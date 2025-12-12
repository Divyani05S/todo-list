# Todo List Manager 📝

A simple, fully-functional CLI application for managing your todo list. **No external API keys required** - everything runs locally!

## Features

- ✅ Add, update, and delete todos
- ✅ Mark todos as completed/pending
- ✅ View all todos or filter by status
- ✅ View statistics (completion rate, counts)
- 💾 Automatic local data persistence (JSON file)
- 🎯 Clean, beginner-friendly code
- 🚀 No external dependencies - uses only Python standard library

## Prerequisites

- Python 3.7 or higher (that's it!)

## Installation

1. **Navigate to the project directory**
   ```bash
   cd todo-list-manager
   ```

2. **That's it!** No dependencies to install - this project uses only Python's standard library.

## Usage

### Run the Application

```bash
python src/main.py
```

### Menu Options

1. **Add a new todo** - Create a new todo item with title and optional description
2. **List all todos** - View all todos (completed and pending)
3. **List pending todos** - View only incomplete todos
4. **Mark todo as completed** - Mark a todo as done
5. **Mark todo as pending** - Unmark a completed todo
6. **Update todo** - Modify a todo's title or description
7. **Delete todo** - Remove a todo (with confirmation)
8. **View statistics** - See completion rate and counts
9. **Exit** - Save and exit the application

## Example Session

```
============================================================
                    TODO LIST MANAGER
============================================================
1. Add a new todo
2. List all todos
3. List pending todos
4. Mark todo as completed
5. Mark todo as pending
6. Update todo
7. Delete todo
8. View statistics
9. Exit
============================================================

Enter your choice (1-9): 1

--- Add New Todo ---
Enter todo title: Buy groceries
Enter description (optional, press Enter to skip): Milk, eggs, bread

[SUCCESS] Todo added successfully!
  ID: 1 - Buy groceries
```

## Project Structure

```
todo-list-manager/
│
├── src/
│   ├── main.py          # Main entry point and CLI interface
│   ├── todo_manager.py  # Todo management logic and data persistence
│   └── display.py       # Display formatting utilities
│
├── todos.json           # Data file (created automatically)
├── requirements.txt     # Dependencies (empty - uses stdlib only)
└── README.md           # This file
```

## Data Storage

All todos are automatically saved to `todos.json` in the project root directory. This file is created automatically when you add your first todo.

**Note:** The `todos.json` file is included in `.gitignore` if you're using version control, so your personal todos won't be committed to the repository.

## Features in Detail

### Todo Properties
Each todo has:
- **ID**: Auto-incremented unique identifier
- **Title**: Required, the main todo text
- **Description**: Optional, additional details
- **Completed**: Boolean status
- **Created At**: Timestamp when created
- **Completed At**: Timestamp when completed (if applicable)

### Statistics
The statistics view shows:
- Total number of todos
- Number of completed todos
- Number of pending todos
- Completion rate percentage

## Error Handling

The application includes comprehensive error handling for:
- Invalid menu choices
- Invalid todo IDs
- Empty todo titles
- File I/O errors
- User input validation

## Example Output

### Listing Todos
```
============================================================
                    TODO LIST
============================================================
[ ] ID: 1 - Buy groceries
[X] ID: 2 - Finish project
[ ] ID: 3 - Call dentist
============================================================
```

### Statistics
```
============================================================
                    STATISTICS
============================================================
Total Todos: 3
Completed: 1
Pending: 2
Completion Rate: 33.3%
============================================================
```

## Tips

- Use descriptive titles for your todos
- Add descriptions for additional context
- Regularly check your statistics to track progress
- Completed todos are preserved for reference

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!
