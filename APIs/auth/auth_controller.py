from flask import jsonify
from APIs.auth.auth_helper import register_validate


def register_controller(data):
    try:
        try:
            if register_validate(data):
                
                user_name = data.get('user_name')
                password = data.get('password')
                email = data.get('email')
                confirm_password = data.get('confirm_password')

            return jsonify({
                'user_name':user_name,
                'password':password,
                'email':email,
                'confirm_password':confirm_password
                }),201
        except ValueError as error:
            return jsonify({'error':str(error)}),400
        except Exception as error:
            return jsonify({'error':str(error)}),500
        
    except Exception as error:
        return jsonify({'error':str(error)})