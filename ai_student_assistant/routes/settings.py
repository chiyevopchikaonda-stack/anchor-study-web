from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    request,
    jsonify,
    url_for
)

from ai_student_assistant.database import get_db


settings = Blueprint("settings", __name__)


@settings.route("/settings")
def settings_page():

    if "user" not in session:

        return redirect(url_for("auth.login"))


    conn = get_db()


    user = conn.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        """,
        (session["user"],)
    ).fetchone()


    conn.close()


    return render_template(
        "settings.html",
        user=user
    )




@settings.route("/save-theme", methods=["POST"])
def save_theme():


    if "user" not in session:

        return jsonify({
            "status":"not logged in"
        })



    data = request.get_json()


    theme = data.get("theme")



    conn = get_db()



    conn.execute(
        """
        UPDATE users
        SET theme=?
        WHERE username=?
        """,
        (
            theme,
            session["user"]
        )
    )


    conn.commit()

    conn.close()



    return jsonify({

        "status":"saved"

    })
