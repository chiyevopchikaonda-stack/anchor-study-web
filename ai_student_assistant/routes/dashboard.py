from flask import Blueprint, render_template, redirect, url_for, session
from ai_student_assistant.database import get_db
from datetime import datetime
from ai_student_assistant.ai_engine import generate_ai_insights
from ai_student_assistant.study_planner import generate_study_plan
from ai_student_assistant.weekly_review import generate_weekly_review


dashboard = Blueprint("dashboard", __name__)



@dashboard.route("/dashboard")
def dashboard_view():

    if "user" not in session:
        return redirect(url_for("auth.login"))


    username = session["user"]

    conn = get_db()


    # ---------------- USER PROFILE ----------------

    user_data = conn.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        """,
        (username,)
    ).fetchone()



    # ---------------- TASKS ----------------

    tasks = conn.execute(
        """
        SELECT *
        FROM tasks
        WHERE username=?

        ORDER BY

        CASE status

            WHEN 'active' THEN 1
            WHEN 'backlog' THEN 2
            WHEN 'done' THEN 3

        END,

        due_date ASC

        """,
        (username,)
    ).fetchall()



    completed_tasks = conn.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE username=?
        AND status='done'
        """,
        (username,)
    ).fetchone()[0]



    total_tasks = len(tasks)



    # ---------------- NOTES ----------------

    note_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM notes
        WHERE username=?
        """,
        (username,)
    ).fetchone()[0]



    # ---------------- RESOURCES ----------------

    resource_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM resources
        WHERE username=?
        """,
        (username,)
        ).fetchone()[0]



    # ---------------- MOOD ----------------

    moods = conn.execute(
        """
        SELECT *
        FROM moods
        WHERE username=?
        ORDER BY created_at DESC
        LIMIT 5
        """,
        (username,)
    ).fetchall()



    mood_data = conn.execute(
        """
        SELECT mood, COUNT(*) AS total
        FROM moods
        WHERE username=?
        GROUP BY mood
        """,
        (username,)
    ).fetchall()



    # ---------------- FOCUS SCORE ----------------

    score = 0


    if total_tasks:
        score += min(completed_tasks * 15, 40)


    if note_count:
        score += 20


    if resource_count:
        score += 20


    if moods:
        score += 20


    if score > 100:
        score = 100




    # ---------------- BIRTHDAY CHECK ----------------

    birthday_message = None


    if user_data["birthday"]:

        today = datetime.now().strftime("%m-%d")

        birthday = user_data["birthday"][5:]


        if today == birthday:

            birthday_message = (
                f"🎉 Happy Birthday, {user_data['full_name']}! "
                "Another year of learning, growing and becoming. "
                "Anchor is celebrating you today 🌱⚓"
            )




    # ---------------- TIME GREETING ----------------

    hour = datetime.now().hour


    if hour < 12:

        greeting = f"Good morning, {user_data['full_name']} ☀️"


    elif hour < 18:

        greeting = f"Good afternoon, {user_data['full_name']} 🌱"


    else:

        greeting = f"Good evening, {user_data['full_name']} 🌙"





    # ---------------- AI INSIGHTS ----------------

    suggestions = generate_ai_insights(
        tasks,
        moods,
        note_count,
        resource_count
    )


    study_plan = generate_study_plan(tasks)


    weekly_review = generate_weekly_review(
        tasks,
        moods,
        note_count,
        resource_count
    )



    if len(tasks) >= 3:

        suggestions.append(
            "You have several tasks waiting. Try completing the most urgent one first."
        )


    if note_count == 0:

        suggestions.append(
            "Create your first study note to start building your knowledge library."
        )


    if resource_count == 0:

        suggestions.append(
            "Upload your lecture materials so your resources stay organised."
        )


    if not suggestions:

        suggestions.append(
            "You're building good habits. Keep showing up consistently."
        )





    # ---------------- ACTIVITY ----------------

    activities = []


    for task in tasks[:3]:

        activities.append(
            {
                "icon": "✅",
                "text": f"Task: {task['title']}"
            }
        )



    for mood in moods[:2]:

        activities.append(
            {
                "icon": "🌤",
                "text": f"Mood logged: {mood['mood']}"
            }
        )

        # ---------------- ANCHIE MESSAGE ----------------

    hour = datetime.now().hour


    if hour < 12:

        time_message = "Good morning ☀️"


    elif hour < 18:

        time_message = "Hope your day is going well 🌱"


    else:

        time_message = "Hope you had a productive day 🌙"



    if len(tasks) >= 5:

        anchie_message = (
            f"{time_message}! "
            "You have a lot on your plate today. "
            "Let's tackle one thing at a time ⚓"
        )


    elif len(tasks) == 0:

        anchie_message = (
            f"{time_message}! "
            "Your study space is empty. "
            "Want to plan your next goal? 📚"
        )


    elif completed_tasks > 0:

        anchie_message = (
            f"{time_message}! "
            "Great job making progress. "
            "Every completed task is a step forward 🌟"
        )


    else:

        anchie_message = (
            f"{time_message}! "
            "I'm here to help you stay organised and focused ⚓"
        )

    conn.close()



    return render_template(

        "index.html",

        user=username,

        profile=user_data,

        tasks=tasks,

        moods=moods,

        mood_data=mood_data,

        suggestions=suggestions,

        study_plan=study_plan,

        focus_score=score,

        greeting=greeting,

        note_count=note_count,

        resource_count=resource_count,

        activities=activities,

        weekly_review=weekly_review,

        birthday_message=birthday_message,

        anchie_message=anchie_message

    )