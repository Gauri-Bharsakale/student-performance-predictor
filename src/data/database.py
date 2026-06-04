
import sqlite3
import pandas as pd

DB_PATH = "data/students.db"

def create_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        studytime INTEGER,
        failures INTEGER,
        absences INTEGER,
        G3 INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_data(df):
    conn = create_connection()
    cursor = conn.cursor()

    records = []

    for _, row in df.iterrows():
        records.append(
            (
                int(row["studytime"]),
                int(row["failures"]),
                int(row["absences"]),
                int(row["G3"])
            )
        )

    cursor.executemany("""
    INSERT INTO students
    (studytime, failures, absences, G3)
    VALUES (?, ?, ?, ?)
    """, records)

    conn.commit()
    conn.close()

def fetch_data():
    conn = create_connection()

    df = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )

    conn.close()

    return df
