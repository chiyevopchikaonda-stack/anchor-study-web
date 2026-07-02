from flask import Flask, render_template, request, redirect, url_for, session
from database import init_db, get_db
import datetime

app = Flask(__name__)
app.secret_key = "anchor-study-secret"

init_db()

verses = [
    {"text": "I can do all things through Christ who strengthens me.", "ref": "Philippians 4:13"},
    {"text": "Be still, and know that I am God.", "ref": "Psalm 46:10"},
    {"text": "Trust in the Lord with all your heart.", "ref": "Proverbs 3:5"},
    {"text": "The Lord is my shepherd; I shall not want.", "ref": "Psalm 23:1"},
    {"text": "God has not given us a spirit of fear, but of power.", "ref": "2 Timothy 1:7"},
    {"text": "Commit your work to the Lord.", "ref": "Proverbs 16:3"},
    {"text": "Be strong and courageous.", "ref": "Joshua 1:9"},
    {"text": "Let your light shine before others.", "ref": "Matthew 5:16"},
]

def get_daily_verse():
    today = datetime.date.today()
    index = today.toordinal() % len(verses)
    return verses[index]

def generate_reflection(verse_text):
    return f"This verse reminds you to stay grounded. In your studies, apply discipline and consistency. Think: how can I align today's tasks with this mindset — {verse_text[:40]}..."

@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
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
            return redirect(url_for("dashboard"))

        return "Invalid credentials"

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
        except:
            return "User already exists"
        finally:
            conn.close()

        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/guest")
def guest():
    session["user"] = "guest"
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]

    conn = get_db()

    tasks = conn.execute(
        "SELECT * FROM tasks WHERE username = ? ORDER BY created_at DESC",
        (user,)
    ).fetchall()

    conn.close()

    return render_template("index.html", user=user, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]
    title = request.form.get("task")

    conn = get_db()

    # Get today's mood
    mood_row = conn.execute(
        "SELECT mood FROM moods WHERE username = ? ORDER BY id DESC LIMIT 1",
        (user,)
    ).fetchone()

    mood = mood_row["mood"] if mood_row else "😐 Neutral"

    limit = get_task_limit(mood)

    active_count = conn.execute(
        "SELECT COUNT(*) as count FROM tasks WHERE username = ? AND status = 'active'",
        (user,)
    ).fetchone()["count"]

    # Decide status
    if active_count >= limit:
        status = "backlog"
    else:
        status = "active"

    conn.execute(
        "INSERT INTO tasks (username, title, status) VALUES (?, ?, ?)",
        (user, title, status)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    conn.execute(
        "UPDATE tasks SET status = 'done' WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]

    conn = get_db()

    if request.method == "POST":
        content = request.form.get("note")
        conn.execute(
            "INSERT INTO notes (username, content) VALUES (?, ?)",
            (user, content)
        )
        conn.commit()

    notes = conn.execute(
        "SELECT * FROM notes WHERE username = ?",
        (user,)
    ).fetchall()

    conn.close()

    return render_template("notes.html", notes=notes, user=user)


@app.route("/settings")
def settings():
    return "<h1>Settings coming soon</h1>"

@app.route("/mood", methods=["GET", "POST"])
def mood():
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]

    conn = get_db()

    if request.method == "POST":
        mood = request.form.get("mood")

        conn.execute(
            "INSERT INTO moods (username, mood) VALUES (?, ?)",
            (user, mood)
        )
        conn.commit()

    moods = conn.execute(
        "SELECT * FROM moods WHERE username = ? ORDER BY id DESC",
        (user,)
    ).fetchall()

    conn.close()

    return render_template("mood.html", moods=moods, user=user)

def get_task_limit(mood):
    if mood in ["😔 Sad", "😴 Tired"]:
        return 2
    elif mood in ["😐 Neutral"]:
        return 4
    elif mood in ["🔥 Motivated"]:
        return 6
    return 3

@app.route("/scriptures")
def scriptures():
    verse = get_daily_verse()
    reflection = generate_reflection(verse["text"])
    return render_template("scriptures.html", verse=verse, reflection=reflection)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)