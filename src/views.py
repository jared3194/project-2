from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("base.html")

# def create_bar_chart():
# note = json.loads(request.data)
# noteID = note['noteID']
# note = Note.query.get(noteID)
# if note:
#     if note.user_id == current_user.id:
#         db.session.delete(note)
#         db.session.commit()