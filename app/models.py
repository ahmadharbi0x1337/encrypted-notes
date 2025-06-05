"""
Databases models for users and encrypted notes.
Uses SQLAlchemy ORM and integrates with Flask-Login
"""
from flask_login import UserMixin
from sqlalchemy.sql import func
# Shared SQLAlchemy instance initialized in app/__init__.py 
from . import db

class User(UserMixin, db.Model):
    """
    Represent a user in the system.
    Inherits from Flask-Login UserMixin to support session tracking.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    # One-to-many relationship: one user can have multiple notes.
    notes = db.relationship('Note', backref='owner', lazy=True)

    def __repr__(self):
        return f"<User: {self.username}>"
    
class Note(db.Model):
    """
    Represent a single encrypted note.
    Each note is linked to a user via a foreign key.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False) # encrypted content
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Note: {self.title[:20]}"