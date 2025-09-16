from flask import render_template
from . import main_bp

@main_bp.route("/")
def landing_page():
    return render_template("landing_page.html")