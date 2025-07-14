# /telegram_bot/db.py

import sqlite3

DB_NAME = 'roulette.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                attempts INTEGER NOT NULL DEFAULT 3
            )
        ''')
        conn.commit()

def add_user_if_not_exists(user_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
            conn.commit()

def get_attempts(user_id: int) -> int:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        res = cursor.execute("SELECT attempts FROM users WHERE user_id = ?", (user_id,)).fetchone()
        return res[0] if res else 0

def update_attempts(user_id: int, new_attempts_count: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET attempts = ? WHERE user_id = ?", (new_attempts_count, user_id))
        conn.commit()