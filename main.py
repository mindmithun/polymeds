from flask import Flask, render_template
from auth.auth import auth
from patient.analytics import patient_analytics

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(patient_analytics)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
