from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'hello',	#wiil do this with environmental variables
        JWT_SECRET_KEY =  'iwR5dcY3HOlvobV82H08FcEh2iqQtyaXfKPlEhu28pI',
        DATABASE='sqlite:///db.sqlite',
    )

    JWTManager(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(error=404, text=str(e)), 404
    
    @app.errorhandler(401)
    def Unauthorised_access(e):
        return jsonify(error=401, text=str(e)), 401
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify(error=500, text=str(e)), 500

    # Register blueprints
    from auth.login import bp as Login
    from auth.signup import bp as Signup

    app.register_blueprint(Login)
    app.register_blueprint(Signup)

    return app
