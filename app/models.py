from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin

# Initialize Database

db = SQLAlchemy()

class User(UserMixin, db.Model):

    """ Define a User class that inherits from both UserMixin and db.Model.
    This means the User class will have user authentication capabilities
    and will represent a database table. """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    notes = db.relationship('Note', backref='owner', lazy=True)
    def __repr__(self):
        return f"<User: {self.username}>"
    
class Note(db.Model):
    """Define A Note Clas """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Note: {self.title}"