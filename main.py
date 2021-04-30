import os
from flask import redirect
from app import make_app

config.py = os.getenv('app_settings')
app - make_app(config.py)

@app.route('/')
def rundoc():
    return redirect('apidocs/')

if __name__ == '__main__':
    app.run(debug = True)