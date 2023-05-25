from flask import Blueprint, render_template
from mods import database


c_to_c = Blueprint("c_to_c", __name__, template_folder="backoffice_templates")


@c_to_c.route("/cat_to_cond")
def cat_to_cond():
    cats = database.get_all_categories()
    conds=database.get_all_conditions()
    return render_template("cat_to_cond.html",cats=cats,conds=conds)