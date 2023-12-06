

def login_model(username):
    data = [
        {'user_name': 'Chandru', 'password': 'chandru'},
            {'user_name': 'Chandru1', 'password': 'chandru1'},
            {'user_name': 'Chandru2', 'password': 'chandru2'}
            ]
    
    for each in data:
        if each['user_name'] == username:
            return each
        
    return None

