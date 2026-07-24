from flask import Blueprint, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from ai_student_assistant.database import get_db

import os


resources = Blueprint("resources", __name__)


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)



@resources.route("/resources", methods=["GET", "POST"])
def resources_page():

    if "user" not in session:
        return redirect("/login")


    username = session["user"]

    conn = get_db()



    if request.method == "POST":

        file = request.files.get("file")


        if file and file.filename:

            filename = secure_filename(file.filename)


            file.save(
                os.path.join(
                    UPLOAD_FOLDER,
                    filename
                )
            )


            conn.execute(
                """
                INSERT INTO resources
                (username, filename)

                VALUES(?,?)
                """,
                (
                    username,
                    filename
                )
            )


            conn.commit()



        conn.close()

        return redirect("/resources")




    cursor = conn.execute(
        """
        SELECT id, filename, uploaded_at
        FROM resources
        WHERE username=?
        ORDER BY uploaded_at DESC
        """,
        (username,)
    )
    
    files = [dict(row) for row in cursor.fetchall()]



    conn.close()



    return render_template(
        "resources.html",
        resources=files
    )





@resources.route("/delete-resource/<int:id>")
def delete_resource(id):

    if "user" not in session:
        return redirect("/login")


    username = session["user"]


    conn = get_db()


    file = conn.execute(
        """
        SELECT filename
        FROM resources
        WHERE id=? AND username=?
        """,
        (
            id,
            username
        )
    ).fetchone()



    if file:

        filepath = os.path.join(
            UPLOAD_FOLDER,
            file["filename"]
        )


        if os.path.exists(filepath):

            os.remove(filepath)



        conn.execute(
            """
            DELETE FROM resources
            WHERE id=? AND username=?
            """,
            (
                id,
                username
            )
        )


        conn.commit()



    conn.close()


    return redirect("/resources")