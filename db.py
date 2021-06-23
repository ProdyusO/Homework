import os
import sqlite3


def execute_query(query, args=()):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    records = cur.fetchall()
    return records


def format_list(lst):
    return '<br>'.join(lst)


def format_records(lst):
    return '<br>'.join(str(lst) for elem in lst)
