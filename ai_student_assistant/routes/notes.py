from flask import Blueprint, render_template, request, redirect, session
from ai_student_assistant.database import get_db


notes = Blueprint("notes", __name__)


@notes.route("/notes", methods=["GET", "POST"])
def notes_page():

    if "user" not in session:
        return redirect("/login")


    username = session["user"]

    conn = get_db()


    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")

        note_id = request.form.get("note_id")


        # UPDATE NOTE

        if note_id:

            conn.execute(
                """
                UPDATE notes
                SET title=?,
                    content=?
                WHERE id=? AND username=?
                """,
                (
                    title,
                    content,
                    note_id,
                    username
                )
            )


        # CREATE NOTE

        else:

            conn.execute(
                """
                INSERT INTO notes
                (username,title,content)

                VALUES(?,?,?)
                """,
                (
                    username,
                    title,
                    content
                )
            )


        conn.commit()

        conn.close()

        return redirect("/notes")



    edit_note=None


    edit_id=request.args.get("edit")


    if edit_id:

        edit_note=conn.execute(
            """
            SELECT *
            FROM notes
            WHERE id=? AND username=?
            """,
            (
                edit_id,
                username
            )
        ).fetchone()



    note_list=conn.execute(
        """
        SELECT *
        FROM notes
        WHERE username=?
        ORDER BY created_at DESC
        """,
        (username,)
    ).fetchall()



    conn.close()



    return render_template(
        "notes.html",
        notes=note_list,
        edit_note=edit_note
    )





@notes.route("/delete-note/<int:id>")
def delete_note(id):

    if "user" not in session:
        return redirect("/login")


    username=session["user"]


    conn=get_db()


    conn.execute(
        """
        DELETE FROM notes
        WHERE id=? AND username=?
        """,
        (
            id,
            username
        )
    )


    conn.commit()

    conn.close()


    return redirect("/notes")