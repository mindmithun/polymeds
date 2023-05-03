from flask import Blueprint, render_template

patient_analytics = Blueprint("patient_analytics", __name__, template_folder="templates")


@patient_analytics.route("/dashboard")
def patient_dashboard():
    return render_template("dashboard.html")
