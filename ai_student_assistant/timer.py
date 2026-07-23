from flask import Blueprint, render_template, request, redirect, session, url_for
from ai_student_assistant.database import get_db

timer = Blueprint("timer", __name__)


@timer.route("/timer")
def timer_page():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    username = session["user"]
    conn = get_db()

    sessions = conn.execute(
        """
        SELECT *
        FROM study_sessions
        WHERE username = ?
        ORDER BY created_at DESC
        LIMIT 5
        """,
        (username,)
    ).fetchall()

    conn.close()

    return render_template(
        "timer.html",
        sessions=sessions
    )


@timer.route("/save_session", methods=["POST"])
def save_session():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    username = session["user"]

    duration = request.form.get("duration")
    subject = request.form.get("subject")
    goal = request.form.get("goal")
    accomplishment = request.form.get("accomplishment")
    notes = request.form.get("notes")

    conn = get_db()

    conn.execute(
        """
        INSERT INTO study_sessions(
            username,
            duration,
            subject,
            goal,
            accomplishment,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            username,
            duration,
            subject,
            goal,
            accomplishment,
            notes
        )
    )

    conn.commit()
    conn.close()

    return redirect("/timer")