from flask import Blueprint, render_template, request, session, redirect
from ai_student_assistant.database import get_db

profile = Blueprint("profile", __name__)


# Edit Profile
@profile.route("/profile/edit", methods=["GET", "POST"])
def edit_profile():

    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    if request.method == "POST":

        conn.execute(
    """
    UPDATE users
    SET
        full_name=?,
        university=?,
        course=?,
        year=?,
        study_goal=?,
        target_gpa=?,
        birthday=?
    WHERE username=?
    """,
    (
        request.form["full_name"],
        request.form["university"],
        request.form["course"],
        request.form["year"],
        request.form["study_goal"],
        request.form["target_gpa"],
        request.form["birthday"],
        session["user"]
    )
)

        conn.commit()

        conn.close()

        return redirect("/settings")

    user = conn.execute(
        "SELECT * FROM users WHERE username=?",
        (session["user"],)
    ).fetchone()

    conn.close()

    return render_template(
        "profile.html",
        user=user
    )