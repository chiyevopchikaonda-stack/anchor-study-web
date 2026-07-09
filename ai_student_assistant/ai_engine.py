from datetime import datetime


def generate_ai_insights(
    tasks,
    moods,
    notes,
    resources
):

    insights = []


    # TASK ANALYSIS

    active_tasks = [
        task for task in tasks
        if task["status"] == "active"
    ]


    overdue_tasks = []


    today = datetime.today().date()


    for task in tasks:

        if task["due_date"]:

            due = datetime.strptime(
                task["due_date"],
                "%Y-%m-%d"
            ).date()


            if due < today and task["status"] != "done":

                overdue_tasks.append(task)



    if overdue_tasks:

        insights.append(
            f"You have {len(overdue_tasks)} overdue task(s). "
            "Try completing the most urgent one first."
        )


    elif active_tasks:

        insights.append(
            f"You currently have {len(active_tasks)} active task(s). "
            "Keep your momentum going."
        )



    else:

        insights.append(
            "Your task list is clear. This is a good time to plan ahead."
        )





    # MOOD ANALYSIS


    stressed = [

        mood for mood in moods
        if "Stressed" in mood["mood"]

    ]


    tired = [

        mood for mood in moods
        if "Tired" in mood["mood"]

    ]



    if len(stressed) >= 3:

        insights.append(
            "You've been feeling stressed often. "
            "Consider taking breaks and studying in smaller sessions."
        )



    elif len(tired) >= 3:

        insights.append(
            "Your energy seems low recently. "
            "Rest is part of productive studying."
        )



    else:

        insights.append(
            "Your mood patterns look balanced. Keep checking in with yourself."
        )





    # NOTES


    if notes == 0:

        insights.append(
            "Start building your knowledge library by adding your first notes."
        )



    else:

        insights.append(
            f"You have {notes} saved note(s). "
            "Reviewing them regularly can strengthen memory."
        )





    # RESOURCES


    if resources == 0:

        insights.append(
            "Upload your lecture materials so Anchor can help organise your resources."
        )


    else:

        insights.append(
            f"You have {resources} resources available for revision."
        )



    return insights