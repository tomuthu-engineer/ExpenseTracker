from API.Auth import auth_blueprint
from API.Auth.auth_controller import login_control

from flask import request

@auth_blueprint.route('/login', methods=['POST'])
def login_view():
    user_name = request.args.get('username')
    password = request.args.get('password')

    print(user_name, 'user_name')
    print(password, 'password')

    return login_control(user_name, password)






