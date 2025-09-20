from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from model.models import User
from dashboard.routes import dashboard_bp
from auth.routes import auth_bp
from profile.routes import profile_bp
from main.routes import main_bp
from model.database import db
from utils.extension import mail

migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")


    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(profile_bp, url_prefix="/profile")
    app.register_blueprint(main_bp)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User,int(user_id))


    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
