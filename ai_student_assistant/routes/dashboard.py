from flask import Blueprint, render_template, redirect, url_for, session
from ai_student_assistant.database import get_db
from ai_student_assistant.smart_insights import generate_study_insights
from ai_student_assistant.study_planner import generate_study_plan
from ai_student_assistant.weekly_review import generate_weekly_review

from datetime import datetime


dashboard = Blueprint("dashboard", __name__)



@dashboard.route("/dashboard")
def dashboard_view():

    if "user" not in session:

        return redirect(
            url_for("auth.login")
        )


    username = session["user"]


    conn = get_db()



    # USER

    user_data = conn.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        """,
        (username,)
    ).fetchone()

    # Safety check: If user record is missing, clear session and redirect to login
    if not user_data:
        conn.close()
        session.pop("user", None)
        return redirect(url_for("auth.login"))



    # TASKS

    tasks = conn.execute(
        """
        SELECT *
        FROM tasks
        WHERE username=?

        ORDER BY due_date ASC

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



    active_tasks = [
        task for task in tasks
        if task["status"] != "done"
    ]



    # NOTES

    note_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM notes
        WHERE username=?
        """,
        (username,)
    ).fetchone()[0]




    # RESOURCES

    resource_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM resources
        WHERE username=?
        """,
        (username,)
    ).fetchone()[0]





    # MOODS

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



    conn.close()



    # FOCUS SCORE

    score = 0


    if tasks:

        score += min(
            int((completed_tasks / len(tasks)) * 50),
            50
        )


    if note_count:

        score += 20


    if resource_count:

        score += 20


    if moods:

        score += 10



    # GREETING & BIRTHDAY CHECK

    full_name = user_data["full_name"] if "full_name" in user_data.keys() else username
    today_date = datetime.now().strftime("%m-%d")
    
    # Assuming there's a 'dob' or 'birth_date' column in YYYY-MM-DD format, or adjust if named differently
    birth_date = user_data.get("dob") or user_data.get("birth_date") if hasattr(user_data, "get") else None
    is_birthday = False

    if birth_date:
        try:
            # Handles YYYY-MM-DD format
            if isinstance(birth_date, str) and len(birth_date) >= 10:
                if birth_date[5:] == today_date:
                    is_birthday = True
        except Exception:
            pass

    if is_birthday:
        greeting = f"Happy Birthday, {full_name}! 🎂🎉"
    else:
        hour = datetime.now().hour

        if hour < 12:

            greeting = (
                f"Good morning, {full_name}"
            )

        elif hour < 18:

            greeting = (
                f"Good afternoon, {full_name}"
            )

        else:

            greeting = (
                f"Good evening, {full_name}"
            )




    # SNAPSHOT

    next_deadline = None


    if active_tasks:

        next_deadline = active_tasks[0]





    # SMART INSIGHTS

    education_level = user_data["education_level"] if "education_level" in user_data.keys() else "General"

    suggestions = generate_study_insights(
        tasks,
        moods,
        note_count,
        resource_count,
        education_level
    )



    study_plan = generate_study_plan(tasks)



    weekly_review = generate_weekly_review(
        tasks,
        moods,
        note_count,
        resource_count
    )



    # ANCHIE

    if is_birthday:
        anchie_message = (
            "Happy Birthday! 🎂 Wishing you a wonderful year filled with growth, "
            "success, and joy. Take some time to celebrate yourself today!"
        )
    elif len(active_tasks) >= 5:

        anchie_message = (
            "You have a busy schedule today. "
            "Choose one important step and begin there."
        )


    elif len(active_tasks) == 0:

        anchie_message = (
            "Your study space is ready. "
            "Set a goal and let's begin."
        )


    elif moods and moods[0]["mood"].lower() in ["tired","stressed"]:

        anchie_message = (
            "Remember to take care of yourself while working toward your goals."
        )


    else:

        anchie_message = (
            "You are building your academic journey one step at a time."
        )



    return render_template(

        "index.html",

        user=username,

        profile=user_data,
        profile_user=user_data,

        tasks=tasks,

        moods=moods,

        suggestions=suggestions,

        study_plan=study_plan,

        weekly_review=weekly_review,

        focus_score=score,

        greeting=greeting,

        note_count=note_count,

        resource_count=resource_count,

        anchie_message=anchie_message,

        next_deadline=next_deadline

    )