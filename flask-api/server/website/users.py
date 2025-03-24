from flask import Blueprint, jsonify, request
from website import db
from .models import User
import uuid


user = Blueprint('user', __name__)


@user.route('/users', methods=['GET'])
def user_list():
    users = User.Query.order_by(User.username).all()
    return jsonify({'status': 'success', 'users': [user.to_json() for user in users]})


@user.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.one_or_404(user, id=user_id)
    return jsonify({'status': 'success', 'user': user.to_json()})


@user.route('/create_user', methods=['POST'])
def create_user():
    post_data = request.get_json()
    user = User()

    user.id = uuid.uuid4().hex
    user.username = post_data.get('username')
    user.email = post_data.get('email')
    #user.posts = 0

    db.session.add(user)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'User created'})


@user.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    post_data = request.get_json()
    user = db.one_or_404(User, id=user_id)

    #add logic if only one is edited
    user.username = request.json('username')
    user.email = request.json('email')
    
    db.session.commit()
    return jsonify({})


@user.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = db.one_or_404(User, id=user_id)

    db.session.delete(user)
    return jsonify({})

