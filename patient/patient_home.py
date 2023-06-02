from flask import Blueprint, render_template

patient_home = Blueprint("patient_home", __name__, template_folder="patient_templates")


@patient_home.route("/patient_dashboard")
def patient_dashboard():
    return render_template("patient_dashboard.html")
