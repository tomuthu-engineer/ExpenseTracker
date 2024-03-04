'''Module providing Authentication functionalities'''
from flask import request,jsonify
from APIs.auth import auth_bp_v1
from APIs.auth.auth_controller import register_controller


@auth_bp_v1.route('/register',methods=['POST'])
def register_view():
    '''function returns response '''
    try:
        
            data = request.get_json()
            return register_controller(data)
            
    except Exception as e:
        return jsonify({"error":"Somthing Went Wrong"}),500
        
        
    
    
