'''Module providing Authentication functionalities'''
from flask import request,jsonify
from APIs.auth import auth_bp_v1
from APIs.auth.auth_controller import is_email_validate,is_password_validate,is_confirm_password,is_login_validate


@auth_bp_v1.route('/register',methods=['POST'])
def register_view():
    '''function returns response '''
    try:

        data = request.json
        if not data or 'userName' not in data:
            return jsonify({'Invalid Request Data':'Username is missing'}),400
        elif not is_email_validate(data['email']) or 'email' not in data:
            return jsonify({'Invalid Request Data':'Email is missing'}),400
        elif not is_password_validate(data['password']) or 'password' not in data:
            return jsonify({'Invalid Request Data':'Password is missing'}),400
        
        username = data.get('userName')

        email = data.get('email') #email validation
        is_valid_email ,message=is_email_validate(email)
        if not is_valid_email:
            return jsonify({'error':message}),400
        
        password = data.get('password') #password validation
        is_valid_password,message=is_password_validate(password)
        if not is_valid_password:
            return jsonify({'error':message}),400
        
        confirm_password = data.get('confirmPassword') #password revalidation
        is_password_matched ,message = is_confirm_password(password,confirm_password)
        if not is_password_matched:
            return jsonify({'error':message}),400

        
        return jsonify({'userName':username,'email':email,'password':password,'confirmPassword':confirm_password}),201
    except ValueError as e :
        return jsonify({'error':str(e)}),500
    
@auth_bp_v1.route("/login",methods=['POST'])
def login_view():
    try :
        data=request.json
        if not data or 'userName' not in data:
            return jsonify({'Invalid Request Data':'Username is missing'}),400
        if not data or 'password' not in data:
            return jsonify({'Invalid Request Data':'Password is missing'}),400
        
        login_userName = data.get('userName')
        login_password = data.get('password')

        is_login,message =is_login_validate(login_userName,login_password)
        if not is_login :
            return jsonify({'error':message}),400

        return jsonify({'userName':login_userName,'password':login_password}),200

    except Exception as e:
        return jsonify({'error',str(e)}),500


    




        
