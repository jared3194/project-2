from flask import render_template, request, redirect, Blueprint
import os.path
from config import conn_str

bp = Blueprint('../templates/views', __name__)

app = Flask(__name__)
app.config['DATABASE_URL'] = conn_str
app.config.update(SECRET_KEY=b'C\xcd\x15t\xaf-\xa3\x80`\xf1!u\xbaBE\x03K\x9d\xdf\xc1\x90H\xf2\xf2/')


@bp.route('/')
def base():
    return render_template("../base.html")

app.run(debug=True, host="127.0.0.1", port=5000)