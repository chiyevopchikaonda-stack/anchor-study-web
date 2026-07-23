from flask import Blueprint, render_template, request, redirect, session, url_for
from datetime import datetime
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
        ORDER BY 
            CASE priority
                WHEN 'High' THEN 1
                WHEN 'Medium' THEN 2
                WHEN 'Low' THEN 3
                ELSE 4
            END,
            due_date ASC
        """,
        (username,)
    ).fetchall()

    completed_list = conn.execute(
    """
    SELECT *
    FROM tasks
    WHERE username = ? AND status = 'done'
    ORDER BY due_date DESC
    """,
    (username,)
).fetchall()

    today = datetime.today().date()
    tasks_with_dates = []

    for task in task_list:
        task_dict = dict(task)

        due = datetime.strptime(
            task_dict["due_date"],
            "%Y-%m-%d"
        ).date()

        difference = (due - today).days

        if task_dict["status"] == "done":
            task_dict["deadline_status"] = "Completed"
        elif difference < 0:
            task_dict["deadline_status"] = "Overdue"
        elif difference == 0:
            task_dict["deadline_status"] = "Due Today"
        elif difference == 1:
            task_dict["deadline_status"] = "Due Tomorrow"
        else:
            task_dict["deadline_status"] = f"Due in {difference} days"

        tasks_with_dates.append(task_dict)

    completed_tasks = conn.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE username = ? AND status = 'done'
        """,
        (username,)
    ).fetchone()[0]

    total_tasks = len(task_list)

    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)
    else:
        progress = 0

    conn.close()

    return render_template(
    "tasks.html",
    tasks=tasks_with_dates,
    completed_tasks=completed_list,
    progress=progress
)


# Add Task
@tasks.route("/add_task", methods=["POST"])
def add_task():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    username = session["user"]
    title = request.form["task"]
    subject = request.form["subject"]
    priority = request.form["priority"]
    due_date = request.form["due_date"]

    conn = get_db()

    conn.execute(
        """
        INSERT INTO tasks(
            username,
            title,
            subject,
            priority,
            due_date,
            status
        )
        VALUES(?, ?, ?, ?, ?, ?)
        """,
        (
            username,
            title,
            subject,
            priority,
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

    if "user" not in session:
        return redirect(url_for("auth.login"))

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

    if "user" not in session:
        return redirect(url_for("auth.login"))

    conn = get_db()

    conn.execute(
        "DELETE FROM tasks WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/tasks")