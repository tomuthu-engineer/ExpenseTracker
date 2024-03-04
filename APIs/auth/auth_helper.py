from flask import jsonify

def register_validate(data):
    try:
        user_name = data.get("user_name")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        
        if user_name is None:
            raise ValueError('Username Is Required')
        
        return True
    except ValueError as error:
        return jsonify({'error':str(error)}),400
    except Exception as error:
        return jsonify({'error':str(error)}),500
        