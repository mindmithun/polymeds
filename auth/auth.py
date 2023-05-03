from flask import Blueprint, render_template, redirect, url_for, request
from mods import database


auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        pwd = request.form["pwd"]
        print(f"username = {username} pwd = {pwd}")
        rows = database.login_user(username, pwd)
        if rows is None:
            print("rows empty")
        return redirect(url_for("patient_analytics.patient_dashboard"))
        # rows = database.login_user(username=username, pwd=pwd)
        # redirect(url_for("patient/dashboard.html"),rows=rows)
    else:
        return "404 Page Not Found"
