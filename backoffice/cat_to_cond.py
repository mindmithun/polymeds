from flask import Blueprint, render_template, request, redirect, url_for
from mods import database


c_to_c = Blueprint("c_to_c", __name__, template_folder="backoffice_templates")


@c_to_c.route("/cat_to_cond" , methods=["GET", "POST"])
def cat_to_cond():    
    if request.method == "POST":
        cat_id = int(request.form["categories"])
        cond_id = request.form.getlist("conditions")
        print(cat_id)
        print(type(cat_id))
        print(cond_id)
        print(len(cond_id))
        if cat_id == 0:
            print("cat 0")
            cats = database.get_all_categories()
            conds = database.get_all_conditions()
            return render_template("cat_to_cond.html",cats=cats,conds=conds,error="Please select a category")

        if len(cond_id) == 0:
            print("cond 0")
            cats = database.get_all_categories()
            conds = database.get_all_conditions()
            return render_template("cat_to_cond.html",cats=cats,conds=conds,error="Please select a condition")

        if (cat_id != 0) and (len(cond_id) != 0):
            sflag = database.link_cat_to_cond(cat_id, cond_id)
            print(sflag)
            cats = database.get_all_categories()
            conds = database.get_all_conditions()
            return render_template("cat_to_cond.html",cats=cats,conds=conds,error=sflag)
    
    cats = database.get_all_categories()
    conds = database.get_all_conditions()
    return render_template("cat_to_cond.html",cats=cats,conds=conds,error="None")