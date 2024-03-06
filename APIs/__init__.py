from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from load_dotenv import DB_URI



app = Flask("Expense Tracker")
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)


def create_app():
    from APIs.auth.auth_view import auth_bp_v1
    app.register_blueprint(auth_bp_v1)
    return app