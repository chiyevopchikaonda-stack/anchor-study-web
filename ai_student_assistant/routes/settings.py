from flask import Blueprint, render_template, session
from ai_student_assistant.database import get_db

settings = Blueprint("settings", __name__)


@settings.route("/settings")
def settings_page():

    if "user" not in session:
        return render_template("login.html")

    username = session["user"]

    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    conn.close()

    return render_template(
        "settings.html",
        user=user
    )