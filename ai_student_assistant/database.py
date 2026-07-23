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

        education_level TEXT,

        institution TEXT,

        study_level TEXT,

        subjects TEXT,

        study_goal TEXT,

        academic_target TEXT,

        username TEXT UNIQUE,

        password TEXT,

        birthday TEXT,

        theme TEXT DEFAULT 'light'

    )
    """)



    # TASKS

    cur.execute("""
CREATE TABLE IF NOT EXISTS tasks(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    title TEXT NOT NULL,

    subject TEXT,

    priority TEXT DEFAULT 'medium',

    due_date TEXT,

    status TEXT DEFAULT 'active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

    # Add new task columns safely

    columns = [
        ("subject", "TEXT"),
        ("priority", "TEXT DEFAULT 'medium'")
    ]

    for column, datatype in columns:
        try:
            cur.execute(
                f"ALTER TABLE tasks ADD COLUMN {column} {datatype}"
            )
        except Exception:
            pass


        # NOTES

    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT NOT NULL,

        title TEXT NOT NULL,

        content TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    # Add subject column safely if it does not exist

    try:
        cur.execute("""
        ALTER TABLE notes ADD COLUMN subject TEXT DEFAULT 'Other'
        """)
    except:
        pass

        

    # MOODS

    cur.execute("""
    CREATE TABLE IF NOT EXISTS moods(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        mood TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # RESOURCES

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

        # STUDY SESSIONS

    conn.execute("""
    CREATE TABLE IF NOT EXISTS study_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        duration INTEGER NOT NULL,
        subject TEXT,
        goal TEXT,
        accomplishment TEXT,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Add new task columns if they don't exist

    try:
        cur.execute("ALTER TABLE tasks ADD COLUMN subject TEXT")
    except:
        pass

    try:
        cur.execute("ALTER TABLE tasks ADD COLUMN description TEXT")
    except:
        pass

    try:
        cur.execute("ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT 'medium'")
    except:
        pass

    conn.commit()

    conn.close()