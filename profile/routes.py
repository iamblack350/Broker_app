import bcrypt
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from model.database import db

from . import profile_bp

@profile_bp.route("/profile")
@login_required
def profile():
    user = current_user
    return render_template("profile.html", user=user)

@profile_bp.route("/upload-profile-picture")
@login_required
def upload_profile_picture():
    return render_template("profile.html")

@profile_bp.route("/edit-profile")
@login_required
def edit_profile():
    return render_template("edit_profile.html")

@profile_bp.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        old_password = request.form.get("current_password", "").strip()
        password = request.form.get("new_password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()

        user = current_user
        old_password_byte = old_password.encode("utf-8")

        if not bcrypt.checkpw(old_password_byte, user.password_hash):
            flash("Your password is incorrect")
            return redirect(request.url)
        if confirm_password != password:
            flash("password do not match")
            return redirect(request.url)

        password_byte = password.encode("utf-8")
        new_password_hash = bcrypt.hashpw(password_byte, bcrypt.gensalt())
        user.password_hash = new_password_hash
        db.session.commit()
        flash("Password has been changed successfully!")
        return redirect(url_for("profile.profile"))
    return render_template("change_password.html")