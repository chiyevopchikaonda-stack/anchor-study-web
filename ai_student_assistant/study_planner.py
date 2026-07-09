from datetime import datetime


def generate_study_plan(tasks):

    today = datetime.today().date()

    urgent = []
    upcoming = []
    completed = []


    for task in tasks:

        if task["status"] == "done":
            completed.append(task)
            continue


        if task["due_date"]:

            due_date = datetime.strptime(
                task["due_date"],
                "%Y-%m-%d"
            ).date()


            days_left = (due_date - today).days


            task_info = {
                "title": task["title"],
                "days": days_left
            }


            if days_left <= 3:

                urgent.append(task_info)


            else:

                upcoming.append(task_info)



    plan = []



    # URGENT TASKS

    if urgent:

        for task in urgent:

            plan.append(
                {
                    "priority":"🔥 High",
                    "title":task["title"],
                    "message":
                    f"Focus on this soon. Deadline is in {task['days']} day(s)."
                }
            )



    # UPCOMING TASKS

    if upcoming:

        for task in upcoming[:3]:

            plan.append(
                {
                    "priority":"📅 Upcoming",
                    "title":task["title"],
                    "message":
                    f"Start preparing early. You have {task['days']} day(s) remaining."
                }
            )



    # NOTHING URGENT

    if not plan:

        plan.append(
            {
                "priority":"🌱 Balanced",
                "title":"No urgent deadlines",
                "message":
                "Use this time to review notes or prepare ahead."
            }
        )



    return plan