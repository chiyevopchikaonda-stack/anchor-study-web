from flask import Blueprint, render_template, request, redirect, session, url_for

from ai_student_assistant.database import get_db


auth = Blueprint("auth", __name__)


# LOGIN

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]


        conn = get_db()


        user = conn.execute(

            """
            SELECT *
            FROM users
            WHERE username=? AND password=?
            """,

            (username, password)

        ).fetchone()


        conn.close()



        if user:

            session["user"] = username

            return redirect(
                url_for("dashboard.dashboard_view")
            )


    return render_template("login.html")





# SIGNUP

@auth.route("/signup", methods=["GET", "POST"])
@auth.route("/register", methods=["GET", "POST"])

def signup():


    if request.method == "POST":


        full_name = request.form["full_name"]

        education_level = request.form["education_level"]

        institution = request.form["institution"]

        study_level = request.form["study_level"]

        subjects = request.form["subjects"]

        study_goal = request.form["study_goal"]

        academic_target = request.form.get(
            "academic_target",
            ""
        )

        username = request.form["username"]

        password = request.form["password"]

        birthday = request.form["birthday"]




        conn = get_db()



        conn.execute(

            """
            INSERT INTO users(

                full_name,

                education_level,

                institution,

                study_level,

                subjects,

                study_goal,

                academic_target,

                username,

                password,

                birthday,

                theme

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?)

            """,

            (

                full_name,

                education_level,

                institution,

                study_level,

                subjects,

                study_goal,

                academic_target,

                username,

                password,

                birthday,

                "light"

            )

        )



        conn.commit()

        conn.close()



        return redirect(
            url_for("auth.login")
        )



    return render_template(
        "signup.html"
    )






# LOGOUT

@auth.route("/logout")

def logout():

    session.clear()

    return redirect(
        url_for("welcome")
    )