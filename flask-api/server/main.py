from api import create_app, db
from flask.cli import FlaskGroup


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5001)