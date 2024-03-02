from flask import jsonify
def auth_register_validation(data):
    try:
        username = data.json('user_name')
        email = data.json('email')

        if username == None:
            raise ValueError("User Name Missing")
        


        # if not username:
        #     return jsonify({"error":"userName is Missing"}),400
        # if not email:
        #     return jsonify({"error":"email is Missing"})
        # if not password:
        #     return jsonify({"error":"passWord is Missing"}),400
        # if not confirm_password:
        #     return jsonify({"error":"confirm_password is Missing"}),400
        # if not is_email_valid(email):
        #     return jsonify({"error":"email should contain @ character "}),400
        # if password != confirm_password:
        #     return jsonify({"error":"password do not match"}),400
    except:
        pass