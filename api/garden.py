import models
from models.garden import Garden
from flask import Blueprint, request, jsonify

bp = Blueprint('garden', __name__,)

@bp.get('/')
def get_gardens():
    gardens = models.storage.all('Garden')
    return jsonify(gardens)
    
@bp.post('/')
def create_garden():
    required = ['user_id','location','description','name']
    body = request.get_json()

    if body is None or body == {}:
        return jsonify({"Status Code": "400", "error": "Missing required fields"}), 400
    
    if len(body) < 4:
        return jsonify({'status_code': 400, 'error': 'missing some reqiured'}), 400
    
    samekeys = [key1 == key2 for key1, key2 in zip(body.keys(), required)]
    if all(samekeys):
        return jsonify({'status_code': 400, 'error': 'missing keys'}), 400
    else:
        new_garden = Garden()
        new_garden.name = body['name']
        new_garden.user_id = body['user_id']
        new_garden.description =  body['description']
        new_garden.save()
        return jsonify({'status_code': 201, 'message': 'Garden created', 'id': new_garden.id})

@bp.get('/<string:garden_id>')
def get_garden_byid(garden_id: str):
    print(type(garden_id))
    garden = models.storage.get('Garden', garden_id)
    print(garden)
    return jsonify(garden.to_dict())
    
@bp.delete('/<string:garden_id>')
def delete_garden(garden_id):
    gardens = models.storage.all('Garden')
    for garden in gardens.values():
        if garden.id == garden_id:
            models.storage.delete(garden)

# @bp.put('/<string:garden_id>')
# def update_garden(garden_id):
#     available_update = ['location', 'description', 'name', 'sensorNo', 'plant']
#     body = request.data

#     if body is None or body == {}:
#         return jsonify({"Status Code": "400", "error": "Missing required fields"}), 400
    
#     key, value = list(body.keys())[0], list(body.values())[1]
#     if key in available_update:
#         garden = models.storage.get('Garden', garden_id)
#         if key == available_update[0]:
#             garden.user_id = value
#         if key == available_update[1]:
#             garden.location = value
#         if key == available_update[2]:
#             garden.description = value
#         if key == available_update[3]:
#             garden.name = value #comming back for put

#             #latter put and get method wil be added for plant and sensors
#             #JWT should be used as authenticator header
#             #other authenticator and verification will be added