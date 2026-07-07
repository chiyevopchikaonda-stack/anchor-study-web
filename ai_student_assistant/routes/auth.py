from tkinter import INSERT

from flask import Blueprint, render_template, request, redirect, url_for, session
from ai_student_assistant.database import get_db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()

        conn.close()

        if user:
            session["user"] = user["username"]
            return redirect(url_for("dashboard.dashboard_view"))

        return "Invalid username or password."

    return render_template("login.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        study_goal = request.form.get("study_goal")
        target_gpa = request.form.get("target_gpa")

        conn = get_db()

        try:
            conn.execute(
                "INSERT INTO users(username,password,study_goal,target_gpa) VALUES (?,?,?,?)",
                (username, password, study_goal, target_gpa)
            )

            conn.commit()

        except:
            conn.close()
            return "Username already exists."

        conn.close()

        return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth.route("/guest")
def guest():

    session["user"] = "Guest"

    return redirect(url_for("dashboard.dashboard_view"))

@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("welcome"))