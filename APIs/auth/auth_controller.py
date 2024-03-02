from flask import jsonify

def register_contorller(data):
    try:
        
        username = data.get("userName")
        email = data.get("email")
        password = data.get("passWord")
        confirm_password = data.get("confirmPassword")

        
        

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

# # def is_password_valid(password):
#     try:
#         if not any(char.isdigit() for char in password):
#             raise ValueError('Password should contain one uppercase')
#         if not any(char.isupper() for char in password):
#             raise ValueError('Password should contain one uppercase')
#         return True
#     except:
#         pass


    