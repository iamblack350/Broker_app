from flask import Blueprint
from model.database import db
from model.models import User
auth_bp = Blueprint("auth", __name__, template_folder="templates")

from . import routes