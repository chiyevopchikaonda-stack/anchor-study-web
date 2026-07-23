from flask import Flask, render_template, send_from_directory, session
from ai_student_assistant.database import get_db

from ai_student_assistant.database import init_db

from ai_student_assistant.routes.auth import auth
from ai_student_assistant.routes.dashboard import dashboard
from ai_student_assistant.routes.notes import notes
from ai_student_assistant.routes.mood import mood
from ai_student_assistant.routes.scriptures import scriptures
from ai_student_assistant.routes.settings import settings
from ai_student_assistant.routes.profile import profile
from ai_student_assistant.routes.tasks import tasks
from ai_student_assistant.routes.resources import resources
from ai_student_assistant.timer import timer


# CREATE APP

app = Flask(
    __name__,
    template_folder="ai_student_assistant/templates",
    static_folder="ai_student_assistant/static"
)

@app.template_filter("format_date")
def format_date(value):

    if not value:
        return ""

    from datetime import datetime

    date = datetime.strptime(
        value,
        "%Y-%m-%d"
    )

    return date.strftime(
        "%d %B %Y"
    )


app.secret_key = "anchor-study-secret"



# INITIALIZE DATABASE

init_db()



# REGISTER BLUEPRINTS

app.register_blueprint(auth)

app.register_blueprint(dashboard)

app.register_blueprint(notes)

app.register_blueprint(mood)

app.register_blueprint(scriptures)

app.register_blueprint(settings)

app.register_blueprint(profile)

app.register_blueprint(tasks)

app.register_blueprint(resources)

app.register_blueprint(timer)



# FILE UPLOADS

@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        "uploads",
        filename
    )



# HOME PAGE

@app.route("/")
def welcome():

    return render_template(
        "welcome.html"
    )

@app.context_processor
def inject_user_profile():
    conn = get_db()

    profile_user = conn.execute(
        "SELECT * FROM users LIMIT 1"
    ).fetchone()

    conn.close()

    return {
        "profile_user": profile_user
    }

# RUN APP
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )