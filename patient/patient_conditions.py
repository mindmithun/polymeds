from flask import Blueprint, render_template, request
from mods import database

Patient_cond = Blueprint("patient_conditions", __name__, template_folder="patient_templates")

@Patient_cond.route("/patient_diseases",methods=['GET','POST'])
def patient_diseases():
    cats = database.get_all_categories()
    return render_template("patient_diseases.html",cats=cats,error="None")