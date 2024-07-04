from flask import Blueprint, request, jsonify
from models._signup import SignUp
from models import storage

bp = Blueprint('auth/signup', __name__)

@bp.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        body = request.get_json()
        
        if "email" not in body and "password" not in body.keys():
            return jsonify({'status_code': 400, 'error': 'email or password missing'})
        
        for user in storage.all('User').values():
            if user.email:
                if body['email'] == user.email:
                    return jsonify({'status_code': 400, 'error': 'email already exist'}), 409
        
        # all authetication and reqierement for sign up will be done here
        # after creating the signup class 
        # try:
        new_signup = SignUp()
        new_signup.email = body['email']
        new_signup.password = body['password']
        new_user = new_signup.create_user()
        new_signup.save()
        print("new user created")
        return jsonify({'status_code': 201, 'message': 'signup successful', 'user': new_user.email}), 201
        # except Exception as e:
        #     print(e)
        #     print("error encounter")
        #     return jsonify({'status_code': 400, 'error': str(e)}), 400
    else:
        return jsonify({'status_code': 400, 'error': 'method not allowed'}), 400