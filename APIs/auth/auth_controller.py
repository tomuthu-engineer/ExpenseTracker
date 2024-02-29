from flask import request,jsonify

def register_contorller(data):
    try:
        data = request.json
        username = data.get("userName")
        email = data.get("email")
        password = data.get("passWord")
        confirm_password = data.get("confirmPassword")

        
        if not username:
            return jsonify({"error":"userName is Missing"}),400
        if not email:
            return jsonify({"error":"email is Missing"})
        if not password:
            return jsonify({"error":"passWord is Missing"}),400
        if not confirm_password:
            return jsonify({"error":"confirm_password is Missing"}),400
        if not is_email_valid(email):
            return jsonify({"error":"email should contain @ character "}),400
        if password != confirm_password:
            return jsonify({"error":"password do not match"}),400

        return jsonify({
            "userName":username,
            "passWord":password,
            "confirmPassword":confirm_password,
            "email":email
        }),201

    except Exception as e:
        return jsonify({"error":str(e)}),500
    
def is_email_valid(email):
    try:
        if '@' not in email:
            return False
        return True
    except Exception as e:
        return jsonify({'error':str(e)}),500

# def is_password_valid(password):
    try:
        if not any(char.isdigit() for char in password):
            raise ValueError('Password should contain one uppercase')
        if not any(char.isupper() for char in password):
            raise ValueError('Password should contain one uppercase')
        return True
    except:
        pass


    