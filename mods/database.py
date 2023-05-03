import sqlite3


def all_users():
    con = sqlite3.connect("./databases/users.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from users")

    rows = cur.fetchall()

    con.close()

    return rows


def login_user(username, pwd):
    con = sqlite3.connect("./databases/users.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from users where username = ? and password = ?", (username, pwd))

    rows = cur.fetchone()
    con.close()

    return rows
