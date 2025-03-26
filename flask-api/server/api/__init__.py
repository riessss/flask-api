import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SECRET_KEY"] = 'A secret'

    db.init_app(app)
    migrate.init_app(app, db)

    from .errors import register_error_hanlders
    register_error_hanlders(app)

    from .users import user
    from .posts import post

    app.register_blueprint(user, url_prefix='/api/user')
    app.register_blueprint(post, url_prefix='/api/post')


    return app

