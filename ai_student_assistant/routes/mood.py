from flask import Blueprint, render_template, request, redirect, url_for, session
from ai_student_assistant.database import get_db

mood = Blueprint("mood", __name__)


@mood.route("/mood", methods=["GET", "POST"])
def mood_page():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    username = session["user"]

    conn = get_db()

    if request.method == "POST":

        selected_mood = request.form["mood"]

        conn.execute(
            """
            INSERT INTO moods(username, mood)
            VALUES (?, ?)
            """,
            (username, selected_mood)
        )

        conn.commit()


    # GET SAVED MOODS
    moods = conn.execute(
        """
        SELECT * FROM moods
        WHERE username = ?
        ORDER BY created_at DESC
        """,
        (username,)
    ).fetchall()


    conn.close()


    return render_template(
        "mood.html",
        moods=moods
    )