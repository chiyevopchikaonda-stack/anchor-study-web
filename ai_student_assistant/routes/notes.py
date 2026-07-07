from flask import Blueprint, render_template

notes = Blueprint("notes", __name__)

@notes.route("/notes")
def notes_page():
    return render_template("notes.html")