def generate_study_insights(
    tasks,
    moods,
    note_count,
    resource_count,
    education_level
):

    insights = []


    active_tasks = [
        task for task in tasks
        if task["status"] != "done"
    ]


    # Task guidance

    if len(active_tasks) >= 5:

        insights.append(
            "You have several tasks waiting. Focus on the most important one first instead of trying to do everything at once."
        )


    elif len(active_tasks) == 0:

        insights.append(
            "Your study space is clear. Add a new goal when you are ready for your next step."
        )


    else:

        insights.append(
            "You are making progress. Keep working through your goals one step at a time."
        )



    # Notes

    if note_count == 0:

        insights.append(
            "Start creating notes to build your personal learning library."
        )


    elif note_count >= 5:

        insights.append(
            "Your notes library is growing. Keep reviewing and organizing your knowledge."
        )



    # Resources

    if resource_count == 0:

        insights.append(
            "Upload your study materials so everything you need stays organised in one place."
        )



    # Education specific

    if education_level == "high_school":

        insights.append(
            "Remember to balance assignments, revision and preparation for upcoming tests."
        )


    elif education_level == "university":

        insights.append(
            "Stay consistent with lectures, coursework and independent study."
        )



    # Mood awareness

    if moods:

        latest_mood = moods[0]["mood"].lower()


        if latest_mood in ["tired", "stressed"]:

            insights.append(
                "Your workload matters, but so does your wellbeing. Take breaks and approach your work calmly."
            )


        elif latest_mood in ["motivated", "happy", "focused"]:

            insights.append(
                "Your current energy is a great opportunity to make progress on your goals."
            )



    return insights