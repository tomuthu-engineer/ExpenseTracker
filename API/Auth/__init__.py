from flask import Blueprint

#creating login blueprint
# user_login=Blueprint('user_login',__name__)



auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')