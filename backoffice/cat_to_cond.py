from flask import Blueprint, render_template
from mods import database


c_to_c = Blueprint("c_to_c", __name__, template_folder="backoffice_templates")


@c_to_c.route("/cat_to_cond")
def cat_to_cond():
    rows = database.get_all_categories()
    return render_template("cat_to_cond.html",rows=rows)