from flask import Blueprint, request, jsonify
from models._login import Login
bp = Blueprint('auth/login', __name__)

@bp.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        body = request.get_json()
        login_attempts = 1
        if "email" not in body and "password" not in body:
            return jsonify({'status_code': 400, 'error': 'email or password missing'})
        else:
            # try:
            new_login = Login()
            auth, user_id = new_login.validate_user(body['email'], body['password'])
            # print(auth)
            if auth == True:
                new_login.login_attempts = login_attempts
                new_login.save()
                login_attempts = 0
                return jsonify({'status_code': 201, 'message': 'login successful', 'User': user_id})
            else:
                return jsonify({'status_code': 400, 'message': 'wrong password', 'login_attempts': login_attempts})
            # except Exception as e:
            #     return jsonify({'status_code': 400, 'error': str(e)})
