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
    cur.execute("select DISTINCT categories from healthsite where isdeleted = 0")
    cat_rows = cur.fetchall()
    con.close()
    return cat_rows


def link_cat_to_cond(cat, cond):
    con = sqlite3.connect("./databases/diseases.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cnd = tuple(cond)
    qry = "update conditions set categoryid={} where key in {}".format(cat,cnd)
    s_flag = cur.execute(qry).rowcount
    con.commit()
    con.close()
    error = str(s_flag) + " rows affected"
    return error


def get_conditions(category):
    con = sqlite3.connect("./databases/diseases.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    qry = "select key, conditions from healthsite where categories = '{}' and isdeleted = 0".format(category)
    cur.execute(qry)
    cond_rows = cur.fetchall()
    con.close()
    return cond_rows