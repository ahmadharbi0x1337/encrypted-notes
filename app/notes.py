"""
Routes for managing encrypted noted (CRUD operations).
Ensures only authenticated users can accessand manipulate their own notes.
"""
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from .models import Note, db
from .crypto import encrypt_note_content, decrypt_note_content

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes')
@login_required
def dashboard():
    """
    Displays the dashboard with a list of the user's decrypted notes.
    """
    notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.timestamp.desc()).all()
    decrypted_notes = []
    for note in notes:
        decrypted_notes.append({
            "id": note.id,
            "title": note.title,
            "content": decrypt_note_content(note.content),
            "timestamp": note.timestamp,
        })
    return render_template('notes.html', notes=decrypted_notes)

@notes_bp.route('/create', methods=["GET", "POST"])
@login_required
def create_note():
    """
    Allow user to create a new encrypted note.
    """
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        if not title.strip() or not content.strip():
            flash("Title and content cannot be empty.")
            return redirect(request.url)

        encrypted_content = encrypt_note_content(content)
        new_note = Note(title=title, content=encrypted_content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()

        flash("Note Created Successfully")
        return redirect(url_for('notes.dashboard'))

    return render_template("create_note.html")

@notes_bp.route('/delete/<int:note_id>')
@login_required
def delete_note(note_id):
    """
    Deletes a note by ID IF the user owns it.
    """
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash("Unauthorized Action.", "danger")
        return redirect(url_for('notes.dashboard'))

    db.session.delete(note)
    db.session.commit()
    flash("Note Deleted Successfully.", "success")
    return redirect(url_for('notes.dashboard'))

@notes_bp.route('/edit/<int:note_id>', methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    """
    Allow a user to edit an existing note.
    """
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash("Unauthorized Action.", "danger")
        return redirect(url_for('notes.dashboard'))

    if request.method == "POST":
        note.title = request.form['title']        
        note.content = encrypt_note_content(request.form['content'])

        if not note.title.strip() or not note.content.strip():
            flash("Title and content cannot be empty.")
            return redirect(request.url)

        db.session.commit()
        flash("Note Updated Successfully!")
        return redirect(url_for('notes.dashboard'))

    decrypted_content = decrypt_note_content(note.content)
    return render_template("edit_note.html", note=note, decrypted_content=decrypted_content)