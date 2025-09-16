from flask import render_template

from . import profile_bp

@profile_bp.route("/profile")
def profile():
    return render_template("profile.html")

@profile_bp.route("/upload-profile-picture")
def upload_profile_picture():
    pass

@profile_bp.route("/edit-profile")
def edit_profile():
    pass

@profile_bp.route("/change-password", methods=["GET", "POST"])
def change_password():
    return render_template("change_password.html")