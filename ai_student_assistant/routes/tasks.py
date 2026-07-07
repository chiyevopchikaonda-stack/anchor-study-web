from flask import Blueprint, render_template, session

tasks = Blueprint("tasks", __name__)


@tasks.route("/tasks")
def tasks_page():

    if "user" not in session:
        return render_template("login.html")

    return render_template(
        "tasks.html",
        user=session["user"]
    )