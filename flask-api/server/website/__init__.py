from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SECRET_KEY"] = 'A secret'

    db.init_app(app)

    from .users import user
    from .posts import post

    app.register_blueprint(user, url_prefix='/api/user')
    app.register_blueprint(post, url_prefix='/api/user')

    with app.app_context():
        db.create_all()

    return app

