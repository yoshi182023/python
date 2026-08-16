from task_manager.task_utils import (
    add_task,
    calculate_progress,
    mark_task_as_complete,
    tasks,
    view_pending_tasks,
)


def show_menu():
    print("\nTask Management System")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            add_task(title, description, due_date)

        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue

            pending_tasks = view_pending_tasks(tasks)
            if not pending_tasks:
                continue

            try:
                task_number = int(input("Enter the pending task number to mark complete: ").strip()) - 1
            except ValueError:
                print("Invalid task number.")
                continue

            if task_number < 0 or task_number >= len(pending_tasks):
                print("Task number out of range.")
                continue

            actual_index = tasks.index(pending_tasks[task_number])
            mark_task_as_complete(actual_index, tasks)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            progress = calculate_progress(tasks)
            completed_count = sum(1 for task in tasks if task.get("completed", False))
            print(f"Task progress: {progress:.2f}% ({completed_count}/{len(tasks)} tasks complete)")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
