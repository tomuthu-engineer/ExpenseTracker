from API.Auth.auth_model import login_model

def login_control(username, password):

    data = login_model(username)
    if data == None:
        return {'unsuccessful': 'User not exists'}
    
    if data['password'] == password:
        return {'successful': 'You are logged in'}
    else:
        return {'unsuccessful': 'incorrect password'}




