from flask import Blueprint, render_template, request, redirect, session, url_for
from ai_student_assistant.database import get_db

auth = Blueprint("auth", __name__)


# Login
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()

        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("dashboard.dashboard_view"))

    return render_template("login.html")



# Signup / Register
@auth.route("/signup", methods=["GET", "POST"])
@auth.route("/register", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        full_name = request.form["full_name"]
        university = request.form["university"]
        course = request.form["course"]
        year = request.form["year"]
        study_goal = request.form["study_goal"]
        target_gpa = request.form["target_gpa"]
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()

        conn.execute(
            """
            INSERT INTO users(
                full_name,
                university,
                course,
                year,
                study_goal,
                target_gpa,
                username,
                password
            )
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                full_name,
                university,
                course,
                year,
                study_goal,
                target_gpa,
                username,
                password
            )
        )

        conn.commit()
        conn.close()

        return redirect(url_for("auth.login"))


    return render_template("signup.html")



# Logout
@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("welcome"))