from APIs.auth import auth_bp_v1

@auth_bp_v1.route('/register',methods=['POST','GET'])
def register_view():
    return {'name':'muthu'}