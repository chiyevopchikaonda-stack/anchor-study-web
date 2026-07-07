from flask import Blueprint, render_template, request, redirect, url_for, session
from ai_student_assistant.database import get_db

profile = Blueprint("profile", __name__)


@profile.route("/profile/edit", methods=["GET", "POST"])
def edit_profile():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    username = session["user"]

    conn = get_db()

    if request.method == "POST":

        study_goal = request.form["study_goal"]
        target_gpa = request.form["target_gpa"]

        conn.execute(
            """
            UPDATE users
            SET study_goal = ?, target_gpa = ?
            WHERE username = ?
            """,
            (study_goal, target_gpa, username)
        )

        conn.commit()

        conn.close()

        return redirect(url_for("settings.settings_page"))


    user = conn.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit_profile.html",
        user=user
    )