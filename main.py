from flask import Flask, render_template
from mods.database import all_users

app = Flask(__name__)

rows = all_users()


@app.route('/')
def home():
    return render_template("index.html", rows=rows)
