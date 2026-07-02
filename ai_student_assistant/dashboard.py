from task_manager import (
    count_tasks,
    get_dashboard_message,
    get_productivity_percentage,
    get_next_task
)


def get_dashboard_data():
    stats = count_tasks()

    next_task = get_next_task()

    if next_task:
        focus = next_task["task"]["task"]
    else:
        focus = "No tasks remaining 🎉"

    return {
        "stats": stats,
        "productivity": get_productivity_percentage(),
        "focus_task": focus,
        "insight": get_dashboard_message()
    }