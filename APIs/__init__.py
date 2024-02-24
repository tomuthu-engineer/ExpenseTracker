from flask import Flask


app = Flask("Expense Tracker")

def create_app():
    from APIs.auth.auth_view import auth_bp_v1
    app.register_blueprint(auth_bp_v1)
    return app