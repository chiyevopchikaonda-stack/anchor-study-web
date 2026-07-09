import sqlite3
import os

DB_NAME = "anchor.db"


print("Using database:", os.path.abspath(DB_NAME))


def get_db():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn



def init_db():

    conn = get_db()

    cur = conn.cursor()



    # USERS

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        university TEXT,
        course TEXT,
        year TEXT,
        study_goal TEXT,
        target_gpa TEXT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)



    # TASKS

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        title TEXT NOT NULL,
        due_date TEXT,
        status TEXT DEFAULT 'active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)



    # NOTES

    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        title TEXT,

        content TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # MOODS

    cur.execute("""
    CREATE TABLE IF NOT EXISTS moods(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        mood TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # RESOURCES  ⭐ NEW

    cur.execute("""
    CREATE TABLE IF NOT EXISTS resources(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        filename TEXT,

        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

# SAVED SCRIPTURES

    cur.execute("""
CREATE TABLE IF NOT EXISTS saved_scriptures(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    verse TEXT,

    reference TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

    conn.commit()

    conn.close()