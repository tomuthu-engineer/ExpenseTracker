'''Module providing Authentication functionalities'''
from flask import request,jsonify
from APIs.auth import auth_bp_v1
from APIs.auth.auth_controller import register_contorller


@auth_bp_v1.route('/register',methods=['POST'])
def register_view():
    '''function returns response '''
    try:
        try:
            data = request.json
            return register_contorller(data)
        except ValueError :
            
    except Exception as e:
        return jsonify({"error":"Somthing Went Wrong"}),500
        
        
    
    
# @auth_bp_v1.route("/login",methods=['POST'])
# def login_view():
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


    




        
