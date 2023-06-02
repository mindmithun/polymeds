from flask import Blueprint, render_template

Patient_cond = Blueprint("patient_conditions", __name__, template_folder="patient_templates")

@Patient_cond.route("/patient_diseases")
def patient_diseases():
    return render_template("patient_diseases.html")