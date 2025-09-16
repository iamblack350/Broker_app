from flask import Blueprint
from . import routes

auth_bp = Blueprint("auth", __name__, template_folder="templates")
