from collections import Counter


def generate_weekly_review(tasks, moods, notes, resources):

    review = {}


    # TASKS

    completed = [

        task for task in tasks

        if task["status"] == "done"

    ]


    review["completed_tasks"] = len(completed)



    # NOTES

    review["notes"] = notes



    # RESOURCES

    review["resources"] = resources



    # MOOD

    if moods:


        mood_list = [

            mood["mood"]

            for mood in moods

        ]


        most_common = Counter(
            mood_list
        ).most_common(1)[0][0]


        review["mood"] = most_common


    else:

        review["mood"] = "No mood data yet"



    # AI MESSAGE


    if len(completed) >= 5:


        message = (
            "Great consistency this week. "
            "Your progress shows that small steps are adding up."
        )


    elif len(completed) > 0:


        message = (
            "You made progress this week. "
            "Try creating a small daily study routine."
        )


    else:


        message = (
            "This week is a fresh start. "
            "Begin with one achievable task."
        )



    review["message"] = message



    return review