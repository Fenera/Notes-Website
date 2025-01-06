from flask import Blueprint, render_template

# user routes(besides authentication)

views = Blueprint('views', __name__)

# homepage
@views.route('/') 
def home():
    return render_template("home.html")


