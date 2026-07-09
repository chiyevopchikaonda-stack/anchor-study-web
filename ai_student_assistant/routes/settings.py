from flask import Blueprint, render_template, session, redirect
from ai_student_assistant.database import get_db

settings = Blueprint("settings", __name__)


# Settings Page
@settings.route("/settings")
def settings_page():

    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE username=?",
        (session["user"],)
    ).fetchone()

    conn.close()

    return render_template(
        "settings.html",
        user=user
    )