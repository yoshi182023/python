from task_manager.validation import (
    get_task_validation_error,
    validate_due_date,
    validate_task_description,
    validate_task_title,
)

# 任务列表：保存所有任务，每个任务都是一个字典
# 这里使用列表来存储多个任务，方便添加、查看和更新
# 任务是动态增长的，使用 append() 向列表中添加新任务
# 也可用 len(tasks) 来获取当前任务总数

tasks = []


# 添加任务时，先调用统一校验函数检查输入是否合法
# 若通过校验，则构造字典并加入 tasks 列表中
# 使用 append() 向任务列表插入一个任务
#
def add_task(title, description, due_date):
    error_message = get_task_validation_error(title, description, due_date)
    if error_message:
        print(error_message)
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


# 标记任务完成：根据索引找到对应任务，然后将 completed 改为 True
# 这里判断 index 是否为 int，如果不是，就尝试转换为整数
# 也检查 index 是否在有效范围内：0 <= index < len(target_tasks)
#
def mark_task_as_complete(index, task_list=None):
    target_tasks = tasks if task_list is None else task_list

    if not isinstance(index, int):
        try:
            index = int(index)
        except (TypeError, ValueError):
            print("Invalid task index.")
            return False

    if index < 0 or index >= len(target_tasks):
        print("Task index out of range.")
        return False

    if target_tasks[index].get("completed"):
        print("Task is already complete.")
        return True

    target_tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True


# 查看未完成任务：遍历任务列表，筛选出 completed 为 False 的任务
# 使用列表推导式 [task for task in target_tasks if not task.get("completed", False)]
# 如果没有待办任务，则打印 "No pending tasks." 并返回空列表
# 否则显示每个任务的标题和截止日期，便于用户快速查看
#
def view_pending_tasks(task_list=None):
    target_tasks = tasks if task_list is None else task_list
    pending_tasks = [task for task in target_tasks if not task.get("completed", False)]

    if not pending_tasks:
        print("No pending tasks.")
        return []

    print("Pending tasks:")
    for idx, task in enumerate(pending_tasks, start=1):
        print(f"{idx}. {task['title']} - Due: {task['due_date']}")

    return pending_tasks


# 计算任务完成进度：
# completed_tasks = sum(1 for task in target_tasks if task.get("completed", False))
# 表示统计已完成任务的数量
# len(target_tasks) 表示总任务数量
# progress = (completed_tasks / len(target_tasks)) * 100
# 可以得到百分比进度，使用 round(..., 2) 保留两位小数
# 如果没有任务，则返回 0，避免除以 0 的错误
#
def calculate_progress(task_list=None):
    target_tasks = tasks if task_list is None else task_list

    if not target_tasks:
        return 0

    completed_tasks = sum(1 for task in target_tasks if task.get("completed", False))
    progress = (completed_tasks / len(target_tasks)) * 100
    return round(progress, 2)
