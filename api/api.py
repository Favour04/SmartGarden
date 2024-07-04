from flask import Blueprint, request, jsonify, abort
from models import storage
# from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("api", __name__)


@bp.route("/", methods=["GET"])
# @jwt_required()
def apiindex():
    # try:
    #     current_user = get_jwt_identity()
    # except:
    #     jsonify({"Status Code": "401", "error": "Unauthorised access to this page"}), 401

    return jsonify({
        "message": "Hello World",
        "current_user": 'hello'
         })