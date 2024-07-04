from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig, TestingConfig, ProductionConfig

app = Flask(__name__, instance_relative_config=True)

env = ''

if env == 'production':
    app.config.from_object(ProductionConfig)
elif env == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)

JWTManager(app)
@app.route('/')
def index():
    return "Hello world"

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
from auth import login
from auth import signup
from api import garden
from api import api
app.register_blueprint(api.bp, url_prefix='/api')
app.register_blueprint(login.bp, url_prefix='/auth')
app.register_blueprint(signup.bp, url_prefix='/auth')
app.register_blueprint(garden.bp, url_prefix='/api/garden')
app.add_url_rule("/", view_func=api.apiindex)

if __name__ == '__main__':
    app.run(debug=True)