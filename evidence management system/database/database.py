import sqlite3

DATABASE = "data/evidence.db"

def create_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evidence (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evidence_number TEXT UNIQUE,
            case_number TEXT,
            description TEXT,
            storage_location TEXT,
            officer TEXT,
            date_logged TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()