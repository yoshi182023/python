from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        return False

    title = title.strip()
    return len(title) >= 3


def validate_task_description(description):
    if not isinstance(description, str):
        return False

    description = description.strip()
    return len(description) >= 5


def validate_due_date(due_date):
    if due_date is None:
        return False

    try:
        if isinstance(due_date, datetime):
            return True

        if isinstance(due_date, str):
            datetime.strptime(due_date.strip(), "%Y-%m-%d")
            return True
    except ValueError:
        return False

    return False