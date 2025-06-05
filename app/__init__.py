"""
application factory and core configuration setup.
Handles database initialization, blueprint registration, and login management.
"""
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# Initializing Extensions Without Binding.
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    """
    Flask application factory.
    Creates and configures the flask app instance.    
    """
    
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind extensions to app
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Define login view for @login_required redirects
    login_manager.login_view = 'auth.login'

    # Creates database tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .auth import auth_bp
    from .notes import notes_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    """
    Loads a user by ID for Flask-Login session management.
    """
    from .models import User
    return User.query.get(int(user_id))
