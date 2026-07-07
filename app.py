from flask import Flask, render_template
from ai_student_assistant.database import init_db
from ai_student_assistant.routes.auth import auth
from ai_student_assistant.routes.dashboard import dashboard
from ai_student_assistant.routes.notes import notes
from ai_student_assistant.routes.mood import mood
from ai_student_assistant.routes.scriptures import scriptures
from ai_student_assistant.routes.settings import settings
from ai_student_assistant.routes.profile import profile
from ai_student_assistant.routes.tasks import tasks

# 1. CREATE APP FIRST
app = Flask(
    __name__,
    template_folder="ai_student_assistant/templates",
    static_folder="ai_student_assistant/static"
)

app.secret_key = "anchor-study-secret"

# 2. INIT DB
init_db()

# 3. REGISTER BLUEPRINTS
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(notes)
app.register_blueprint(mood)
app.register_blueprint(scriptures)
app.register_blueprint(settings)
app.register_blueprint(profile)
app.register_blueprint(tasks)

# 4. MAIN PAGE
@app.route("/")
def welcome():
    return render_template("welcome.html")


# 5. RUN
if __name__ == "__main__":
    app.run(debug=True)