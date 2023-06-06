from flask import Blueprint, render_template, request
from mods import database

Patient_cond = Blueprint("patient_conditions", __name__, template_folder="patient_templates")

@Patient_cond.route("/patient_diseases",methods=['GET','POST'])
def patient_diseases():
    if request.method == 'POST':
        categories= request.form['categories']
        cond=database.get_conditions(category=categories)
        cats = database.get_all_categories()
        if not cond:
            error = "No conditions found for category " + categories
        else:
            error = "None"
        return render_template("patient_diseases.html",cond=cond,cats=cats,error= error)
    
    cats = database.get_all_categories()
    return render_template("patient_diseases.html",cats=cats,error="None")