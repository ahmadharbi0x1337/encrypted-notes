from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from .models import User, db

login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    app.bcrypt = bcrypt

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = "warning"

    with app.app_context():
        db.create_all()

    from .auth import auth_bp
    from .notes import notes_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
