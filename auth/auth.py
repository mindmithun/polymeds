from flask import Blueprint, render_template, redirect, url_for, request, session
from mods import database


auth = Blueprint("auth", __name__, template_folder="auth_templates")


def set_session(rows):
    session["key"] = rows["key"]
    session["username"] = rows["username"]
    session["firstname"] = rows["firstname"]
    session["lastname"] = rows["lastname"]
    session["sex"] = rows["sex"]
    session["dob"] = rows["dob"]
    return True


def clear_session(username):
    session.pop("key", None)
    session.pop("username", None)
    session.pop("firstname", None)
    session.pop("lastname", None)
    session.pop("sex", None)
    session.pop("dob", None)
    return True


@auth.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        pwd = request.form["pwd"]
        ses, pop = False, False
        if "username" in session:
            pop = clear_session(username)
        # if not pop:
        #     return render_template("login.html", error = "Error clearing session")
        rows = database.login_user(username, pwd)
        if rows is None:
            return render_template("login.html", error = "Username or Password is incorrect")
        ses = set_session(rows)
        if not ses:
            return render_template("login.html", error = "Error creating session")
        
        return redirect(url_for("patient_analytics.patient_dashboard"))
    else:
        #TODO: Rewrite Logic of this later. Unreachable code.
        return "404 Page Not Found"


@auth.route("/logout")
def logout():
    if "username" not in session:
        clear_session(username)
    return redirect(url_for("auth.login"))