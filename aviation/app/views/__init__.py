from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import config_settings
from models.user import db
from views.index import Hello

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config_setting['development'])

    app = Api(app)
    app.add.resouce(Hello, '/')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false
    
    db.init_app(app)
    migrate.init_app(app, db)

    return app