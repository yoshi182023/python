from datetime import datetime


# 任务标题校验：必须是字符串，并且去掉空格后长度至少为 3
# 这里使用 len(title) >= 3 来保证标题不会过短，避免空值或单字符标题
# 如果类型不是 str，直接返回 False
def validate_task_title(title):
    if not isinstance(title, str):
        return False

    title = title.strip()
    return len(title) >= 3


# 任务描述校验：必须是字符串，并且去掉空格后长度至少为 5
# 这里用 len(description) >= 5 作为最基本要求，保证描述内容足够清楚
# 也避免用户输入空字符串或过短说明
def validate_task_description(description):
    if not isinstance(description, str):
        return False

    description = description.strip()
    return len(description) >= 5


# 截止日期校验：确保输入是有效的 YYYY-MM-DD 格式
# 通过 datetime.strptime(due_date, "%Y-%m-%d") 进行严格格式校验
# 如果输入为空、非字符串或格式不合法，则返回 False
# 例如：2026-08-20 是合法，not-a-date 是非法
def validate_due_date(due_date):
    if due_date is None:
        return False

    try:
        if isinstance(due_date, datetime):
            return True

        if isinstance(due_date, str):
            due_date = due_date.strip()
            if not due_date:
                return False
            datetime.strptime(due_date, "%Y-%m-%d")
            return True
    except ValueError:
        return False

    return False


# 统一校验入口：检查标题、描述、截止日期，并返回对应错误信息
# 这样可以在添加任务之前一并检查，并提供更友好的提示信息
# 对应的错误信息会在 task_utils.py 中被打印给用户
def get_task_validation_error(title, description, due_date):
    if not validate_task_title(title):
        return "Invalid title. It must contain at least 3 characters."

    if not validate_task_description(description):
        return "Invalid description. It must contain at least 5 characters."

    if not validate_due_date(due_date):
        return "Invalid due date. Use the format YYYY-MM-DD."

    return None
