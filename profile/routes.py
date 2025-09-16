from . import profile_bp

@profile_bp.route("/profile")
def profile():
    pass

@profile_bp.route("/upload-profile-picture")
def upload_profile_picture():
    pass

@profile_bp.route("/edit-profile")
def edit_profile():
    pass