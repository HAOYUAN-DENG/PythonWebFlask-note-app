from flask import Blueprint, render_template, request, flash, jsonify

from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added successfully!", category="success")

    return render_template("home.html", user=current_user)


@views.route("/delete-note", methods=['POST'])
@login_required
def delete_note():
    note_id = request.json.get('id')
    note = Note.query.get(note_id)
    # It checks if the note exists and if the current user is the owner of the note.
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash("Note deleted successfully!", category="success")
        else:
            flash("You do not have permission to delete note!", category="error")
    else:
        flash("Note not found!", category="error")
