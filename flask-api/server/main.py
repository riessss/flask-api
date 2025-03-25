from website import create_app, db
from website.models import User

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True, port=5001)