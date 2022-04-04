########################################
#* FLASK APPLICATION
########################################

# extensions that allow specific classes and functions.
from flask import Flask, Blueprint, render_template, url_for, redirect

# a 'blueprint' of the website structure.
views = Blueprint(__name__, "views")

# the website is defined as a flask app and the url prefix is set to '/'.
app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")

########################################
#* APPLICATION PAGES
########################################

# this is how the homepage is accessed.
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jordan")
def jordan_page():
    return render_template("jordan.html",user_name = "Jordan", favourite_thing = "Coffee")

@app.route("/katy")
def katy_page():
    return render_template("katy.html", user_name = "Katy", favourite_thing = "Fish")

@app.route("/ayesha")
def ayesha_page():
    return render_template("ayesha.html", user_name = "Ayesha", favourite_thing = "Chocolate")

########################################

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

########################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

########################################

# debugging is activated and the project is set to hosted on port 8000 (debugging should only be used in testing).
if __name__ == "__main__":
    app.run(debug=True, port=8000)

########################################