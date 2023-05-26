from flask import Blueprint, render_template, request, redirect, url_for
from mods import database


c_to_c = Blueprint("c_to_c", __name__, template_folder="backoffice_templates")


@c_to_c.route("/cat_to_cond" , methods=["GET", "POST"])
def cat_to_cond():
    if request.method == "POST":
        cat_id = request.form["categories"]
        cond_id = request.form.getlist("conditions")
        print(cat_id)
        print(cond_id)
        return redirect(url_for(".cat_to_cond", error="success"))
    cats = database.get_all_categories()
    conds=database.get_all_conditions()
    return render_template("cat_to_cond.html",cats=cats,conds=conds)