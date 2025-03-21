from flask import Blueprint, jsonify
from website import db
from models import User

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def user_list():
    #all_users = users.all_username()
    return jsonify('''all_users'''), 200

@user.route('/get_user/<int:user_id>', methods=['GET'])
def get_user():
    #one_user = users.one_user(user_id)
    return jsonify(), 200

@user.route('/create_user/<int:user_id>', methods=['POST'])
def create_user():
    user = User(
        username = 
        email = 
        id = 
    )
    new_user = {

    }

    return jsonify(), 200

@user.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user():
    
    return jsonify(), 200

@user.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user():

    return jsonify(), 200

