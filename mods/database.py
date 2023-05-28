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


def get_all_categories():
    con = sqlite3.connect("./databases/diseases.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from categories")
    rows = cur.fetchall()
    con.close()
    return rows


def get_all_conditions():
    con = sqlite3.connect("./databases/diseases.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from conditions  where categoryid=0")
    rows = cur.fetchall()
    con.close()
    return rows

def link_cat_to_cond(cat, cond):
    con = sqlite3.connect("./databases/diseases.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cnd = tuple(cond)
    qry = "update conditions set categoryid={} where key in {}".format(cat,cnd)
    print(qry)
    s_flag = cur.execute(qry).rowcount
    con.commit()
    con.close()
    error = str(s_flag) + " rows affected"
    return error