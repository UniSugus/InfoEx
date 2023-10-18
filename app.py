from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key="UniSugus888"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    if 'name_input' in request.form:
        name = request.form['name_input']
        flash(f"Hi {name}, great to see you!")
    return render_template("index.html")