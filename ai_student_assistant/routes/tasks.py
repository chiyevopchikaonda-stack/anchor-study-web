from flask import Blueprint, render_template, request, redirect, session, url_for
from ai_student_assistant.database import get_db

tasks = Blueprint("tasks", __name__)


# Display Tasks
@tasks.route("/tasks")
def task_page():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    username = session["user"]

    conn = get_db()

    task_list = conn.execute(
        """
        SELECT *
        FROM tasks
        WHERE username = ?
        ORDER BY due_date ASC
        """,
        (username,)
    ).fetchall()

    conn.close()

    return render_template(
        "tasks.html",
        tasks=task_list
    )


# Add Task
@tasks.route("/add_task", methods=["POST"])
def add_task():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    username = session["user"]

    title = request.form["task"]
    due_date = request.form["due_date"]

    conn = get_db()

    conn.execute(
        """
        INSERT INTO tasks(username, title, due_date, status)
        VALUES(?,?,?,?)
        """,
        (
            username,
            title,
            due_date,
            "active"
        )
    )

    conn.commit()
    conn.close()

    return redirect("/tasks")


# Complete Task
@tasks.route("/complete/<int:id>")
def complete_task(id):

    conn = get_db()

    conn.execute(
        "UPDATE tasks SET status='done' WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/tasks")


# Delete Task
@tasks.route("/delete/<int:id>")
def delete_task(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM tasks WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/tasks")