from flask import Blueprint, render_template, redirect, url_for, session
from ai_student_assistant.database import get_db


dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
def dashboard_view():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    user = session["user"]

    conn = get_db()

    # Get user's tasks
    tasks = conn.execute(
        """
        SELECT *
        FROM tasks
        WHERE username = ?
        ORDER BY created_at DESC
        """,
        (user,)
    ).fetchall()


    # Get user's moods
    mood_data = conn.execute(
        """
        SELECT mood, COUNT(*) as total
        FROM moods
        WHERE username = ?
        GROUP BY mood
        """,
        (user,)
    ).fetchall()


    # Count stressful moods
    stress_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM moods
        WHERE username = ?
        AND mood LIKE '%Stress%'
        """,
        (user,)
    ).fetchone()[0]


    # AI mood suggestion
    if stress_count >= 3:

        mood_message = (
            "You've been feeling stressed recently. "
            "Try focusing on one small task first and take a short break."
        )

    elif stress_count == 0:

        mood_message = (
            "Your mood looks balanced. "
            "Keep building your momentum!"
        )

    else:

        mood_message = (
            "Keep checking in with yourself. "
            "Small progress still counts."
        )


    conn.close()


    return render_template(
        "index.html",
        user=user,
        tasks=tasks,
        mood_data=mood_data,
        mood_message=mood_message
    )