from flask import Blueprint, render_template, request, redirect, url_for
from mods import database


c_to_c = Blueprint("c_to_c", __name__, template_folder="backoffice_templates")


@c_to_c.route("/cat_to_cond" , methods=["GET", "POST"])
def cat_to_cond():    
    # TODO:Change all redirect to render_template
    # TODO: Sort out cat empty scenario
    if request.method == "POST":
        cat_id = request.form["categories"]
        cond_id = request.form.getlist("conditions")
        print(cat_id)
        print(cond_id)
        if cat_id == 0:
            print("cat 0")
            return redirect(url_for(".cat_to_cond", error="Select a category"))
        if cond_id == []:
            print("cond 0")
            return redirect(url_for(".cat_to_cond", error="Select a condition"))
        sflag=database.link_cat_to_cond(cat_id, cond_id)
        print(sflag)
        return redirect(url_for(".cat_to_cond", error=sflag))
        
        return redirect(url_for(".cat_to_cond", error="success"))
    cats = database.get_all_categories()
    conds=database.get_all_conditions()
    return render_template("cat_to_cond.html",cats=cats,conds=conds,error="None")