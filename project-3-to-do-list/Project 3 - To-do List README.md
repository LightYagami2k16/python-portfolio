# ✅ To-Do List

A simple to-do list that saves your tasks to a file so they're still there the next time you open the program.

## What it does

- Add new tasks
- View all your tasks (with numbers)
- Mark a task as done ✓
- Delete a task
- Saves everything to `tasks.txt` automatically

## How to run it

```bash
python todo.py
```

## Example

```
=== To-Do List ===
1. Add a task
2. View all tasks
3. Mark a task as done
4. Delete a task
5. Quit

Choice: 1
Enter your task: Learn Python functions
Task added!

Choice: 2
Your tasks:
  1. [ ] Learn Python functions
  2. [✓] Read chapter 3

Choice: 3
Enter task number to mark as done: 1
"Learn Python functions" marked as done!
```

## Python concepts used

- `list` to store tasks in memory
- Reading and writing text files (`open`, `.read()`, `.write()`)
- `for` loop to display all tasks
- `if / elif / else` for the menu
- `while True` to keep the program running
- `strip()` and `split()` to process text from the file
