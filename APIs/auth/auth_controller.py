

def is_email_validate(email):
    try:
        if '@' in email:
            return True,'Email valid'
        else:
            return False,'Email should contain @ character'
    except ValueError as e:
        return False,str(e)

def is_password_validate(password):
    try:
        if len(password)<8:
            return  False, "Password must be at least 8 characters long"

        if not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter"
        
        if not any(char.islower() for char in password):
            return False, "Password must contain at least one lowercase letter"
        
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit"
            
        if password.isalnum():
            return False, "Password must contain at least one special character"
        
        return True,"Password valid"
    
    except ValueError as e:
        return False,str(e)

def is_confirm_password(password,confirm_pasword):
    try :
        if password != confirm_pasword:
            return False,"Password do not match"
        else :
            return True,"Pasword Matched"
    except ValueError as e :
        return False,str(e)
        


def is_login_validate(login_userName,login_password):  
    try :
        
        if username==login_userName and password==login_password:
            return True ,"Login Sucessfull"
        else :
            return False ,"Login Unsucessfull"
    except ValueError as e:
        return False ,str(e)
          

        

        
