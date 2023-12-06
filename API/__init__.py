from flask import Flask

# Creating a Flask app Instance
app= Flask("Expense Tracker")


#creating  factory function
def create_app():

    from API.Auth.auth_view import auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app