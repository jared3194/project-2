from flask import render_template, request, redirect, Blueprint
import os.path
from config import conn_str

bp = Blueprint('views', __name__)

app = Flask(__name__)
app.config['DATABASE_URL'] = conn_str
app.config.update(SECRET_KEY=b'C\xcd\x15t\xaf-\xa3\x80`\xf1!u\xbaBE\x03K\x9d\xdf\xc1\x90H\xf2\xf2/')

db= SQLAlchemy(app)

class airport(db.Model):
        _tablename_ = 'airports'

        airport_id = db.Column(db.Interger, primary_key=True)
        airport = db.Column(db.String(length=50))
        iata = db.Column(db.String(length=5))
        icao = db.Column(db.String(length=5))
        timezone = db.Column(db.String(length = 25))


@bp.route('/')
def base():
    return render_template("base.html", airportflask=airports.query.all())

app.run(debug=True, host="127.0.0.1", port=5000)