from flask import Blueprint
from . import routes

profile_bp = Blueprint("profile", __name__, template_folder="templates")
