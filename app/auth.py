from flask import Blueprint, redirect, render_template, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, db
from app import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username Already Exists')
            return redirect(url_for('auth.register'))
        
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        flash("Account Created Successfully, Please Log in.")
        return redirect(url_for('auth.login'))
    return render_template("register.html")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('notes.dashboard'))
        else:
            flash("Invalid Username or Password")
            return redirect(url_for('auth.login'))
        
    return render_template('login.html')

@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out Successfully')
    return redirect(url_for('auth.login'))

