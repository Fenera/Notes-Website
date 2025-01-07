from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


# user routes(besides authentication)

views = Blueprint('views', __name__)

# homepage
@views.route('/', methods = ['GET', 'POST']) 
@login_required # cannot go to the homepage unless logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note is too short", category = 'error')
        else:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note) # store note in database
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user = current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data) # loaded as a json object(~python dictionary)
    noteId = note['noteId'] # access note id attribute
    note = Note.query.get(noteId) # look for note with that id
    if note: # exists?
        if note.user_id == current_user.id: # check if the user owns that note
            db.session.delete(note) # delete the note
            db.session.commit()
    
    return jsonify({}) 


