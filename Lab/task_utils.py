from datetime import datetime

try:
    from validation import (
        validate_task_description,
        validate_task_title,
        validate_due_date,
    )
except ImportError:
    from Lab.validation import (
        validate_task_description,
        validate_task_title,
        validate_due_date,
    )

# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title. It must contain at least 3 characters.")
        return False

    if not validate_task_description(description):
        print("Invalid description. It must contain at least 5 characters.")
        return False

    if not validate_due_date(due_date):
        print("Invalid due date. Use the format YYYY-MM-DD.")
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip() if isinstance(due_date, str) else due_date,
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")
    return True


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int):
        try:
            index = int(index)
        except (TypeError, ValueError):
            print("Invalid task index.")
            return False

    if index < 0 or index >= len(tasks):
        print("Task index out of range.")
        return False

    if tasks[index].get("completed"):
        print("Task is already complete.")
        return True

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task.get("completed", False)]

    if not pending_tasks:
        print("No pending tasks.")
        return []

    print("Pending tasks:")
    for idx, task in enumerate(pending_tasks, start=1):
        print(f"{idx}. {task['title']} - Due: {task['due_date']}")

    return pending_tasks


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0

    completed_tasks = sum(1 for task in tasks if task.get("completed", False))
    progress = (completed_tasks / len(tasks)) * 100
    return round(progress, 2)