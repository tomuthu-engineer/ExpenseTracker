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
        if not is_email_valid(email):
            raise ValueError('Email is not valid ')
        return True
    


def is_email_valid(email):
    if '@' in email:
        return True
    