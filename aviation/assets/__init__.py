from flask import Flask

def create_app(test_congif=None):
    app = Flask(__name__)
    app.config.update(SECRET_KEY=b'C\xcd\x15t\xaf-\xa3\x80`\xf1!u\xbaBE\x03K\x9d\xdf\xc1\x90H\xf2\xf2/')

    from . import views
    app.register_blueprint(views.bp)

    return app