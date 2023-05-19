from flask import Flask, render_template
from auth.auth import auth
from patient.analytics import patient_analytics
from backoffice.cat_to_cond import c_to_c

app = Flask(__name__)
app.secret_key = 'TODO:change this'


app.register_blueprint(auth)
app.register_blueprint(patient_analytics)
app.register_blueprint(c_to_c)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug)
