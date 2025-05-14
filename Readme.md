# 📝 Task Tracker CLI

**Task Tracker** is a simple, terminal-based Task Management System built with Python. It allows users to add, view, edit, and delete tasks easily from the command line, storing all data in a local JSON file.

---

## 📦 Features

-  Add new tasks with title, description, and status
-  Edit existing tasks
-  Delete specific tasks or clear all tasks
-  List all tasks
-  Filter by status: `In Progress` or `Completed`
-  Timestamped creation and last update info

---

##  File Structure

.
├── task_tracker.py # Main Python script
├── Tasks.json # JSON file to store all tasks (auto-generated)
└── README.md # Documentation


---

## 🚀 How to Run

### Requirements
- Python 3.x installed on your system

### Running the App

python task_tracker.py

Once run, you'll see:

T-A-S-K- T-R-A-C-K-E-R  M-E-N-U
Add task
list task
edit task
delete task
inprogress tasks
completed tasks

Choose an option by typing its name (e.g., add task) and follow the prompts.
🧠 Usage Tips

    Task titles are used as unique identifiers (IDs), so avoid duplicates.

    Use lowercase when prompted (e.g., status should be inprogress or completed).

    The app includes simple delays (using time.sleep) to simulate progress feedback.

    All task data is stored in Tasks.json. Deleting/clearing modifies this file directly.

🔧 Potential Improvements

    Input validation & sanitization

    Use UUIDs or incremental IDs instead of task titles

    GUI or web interface

    Search or sort functionality

    Color-coded CLI interface using libraries like rich or colorama

📜 License

This project is open-source and free to use under the MIT License.

💡 Author
https://github.com/purposewalks9/task-tracker.git
Developed by @purposewalks9
