import sqlite3

DATABASE = "data/evidence.db"

def add_evidence(
        evidence_number,
        case_number,
        description,
        location,
        officer
    ):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO evidence
    (
        evidence_number,
        case_number,
        description,
        storage_location,
        officer
    )
    
    VALUES (?, ?, ?, ?, ?)
    
    """,
    
    (
        evidence_number,
        case_number,
        description,
        location,
        officer
    ))

    conn.commit()
    conn.close()

def view_all_evidence():
    conn = sqlite3.conncet(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM evidence"
    )

    records = cursor.fetchall()

    conn.close()

    return records

def search_evidence(
    evidence_number
):
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM evidence
        WHERE evidence_number = ?
    """,
    (evidence_number,)
    )

    result = cursor.fetchone()

    conn.close()

    return result

def delete_evidence(
     evidence_number
):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM evidence
        WHERE evidence_number = ?
    """,
    (evidence_number,)
    )

    conn.commit()
    conn.close()