from flask import Flask

# Creating a Flask app Instance
app= Flask("Expense Tracker")

#creating  factory function
def create_app():
    return app