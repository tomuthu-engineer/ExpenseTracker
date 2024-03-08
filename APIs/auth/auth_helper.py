from flask import jsonify

def register_validate(data):
    
        user_name = data.get("user_name")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        
        if user_name == None:
            raise ValueError('Username Is Required')
        if email == None:
            raise ValueError('Email is required')
        if password == None:
            raise ValueError('Password is required')
        if confirm_password == None:
            raise ValueError('Confirm password is required')   
        if password != confirm_password:
            raise ValueError("Password don't match")
        if not is_email_valid(email):
            raise ValueError('Email is not valid ')
        if  is_password_valid(password):
             return jsonify({'error':password})
        return True
    


def is_email_valid(email):
    if '@' in email:
        return True
    
def is_password_valid(password):
    
    if not any(char.isdigit() for char in password):
      raise ValueError('Password should contain one digit character')
    if not any(char.isupper() for char in password):
        raise ValueError('Password should contain one uppercase character ')
    if not any(char.islower() for char in password):
        raise ValueError('Password should contain one lowercase character')
