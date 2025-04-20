# 🧠 Task Manager

**Task Manager** is a Django-based web application designed to manage tasks and user assignments within an organization. It allows administrators and team members to create tasks, assign them to workers, set deadlines and priorities, and track task completion.

---

## 🚀 Features

- Create, update, and delete tasks
- Assign multiple workers to each task
- Set task types and priorities (`Low`, `Medium`, `High`, `Critical`)
- Mark tasks as completed or pending
- Custom user model (`Worker`) based on Django’s `AbstractUser`
- Manage worker positions (e.g., Developer, Manager)
- Sort tasks alphabetically

---

## 🛠️ Technologies Used

- Python 3
- Django (4.x)
- SQLite (for development)
- `python-dotenv` for environment variable management
- Bootstrap (optional for frontend styling)

---

## 📦 Models Overview

### 🔹 `Position`

Represents the job title of a worker (e.g., Developer, QA, Manager).

```python
name = models.CharField(max_length=30)
```

---
### 🔹`TaskType`
Defines the category or type of a task (e.g., Bug, Feature, Research).

```python
name = models.CharField(max_length=30)
```
---

### 🔹`Worker` (extends AbstractUser)
Custom user model extended with an optional foreign key to Position.

```python

position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="worker", null=True, blank=True)
```
Inherits username, email, first_name, last_name from AbstractUser

Has get_absolute_url() for detail view

Custom __str__: shows username and email

---

### 🔹` Task` 
Core model representing a task assigned to one or more workers.

```python

name = models.CharField(max_length=255)
description = models.TextField()
deadline = models.DateTimeField()
is_completed = models.BooleanField(default=False)
task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="task")
assignees = models.ManyToManyField(Worker, related_name="task")
priority = models.CharField(
    choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High"), ("Critical", "Critical")],
    max_length=10,
    default="Low"
)
```


Meta.ordering = ["name"] (tasks sorted alphabetically)

Custom __str__ returns a summary of the task and assignees

---

🧪 ` Example Usage` 
---

Add worker positions: e.g., "Developer", "Project Manager"

Add task types: e.g., "Bug", "Feature"

Create a new task and assign one or more workers to it

Set a deadline and select a priority

Mark the task as complete when finished

---

📁 ` Project Structure` 
---


manager/models.py – contains all models: Position, TaskType, Worker, Task

requirements.txt – lists required packages

.env – environment variables (not tracked by git)

README.md – project documentation

settings.py – modified to load secret key from .env

🔐 Security
This project uses environment variables to store sensitive data such as SECRET_KEY.
Make sure .env is listed in .gitignore to avoid exposing credentials.

```python

# settings.py
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
```
---

## 👤 ` Author` 
Developed by Nazarii Khalimonov
https://github.com/Carn1vor3
