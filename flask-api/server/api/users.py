from flask import Blueprint, jsonify, request, abort
from api import db
from .models import User


user = Blueprint('user', __name__)


@user.route('/', methods=['GET'])
def user_list():
    users = User.query.order_by(User.username).all()
    users = []
    if not users:
        abort(404, description="No users found")

    return jsonify({'status': 'success', 'users': [user.to_json() for user in users]}), 200


@user.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).one_or_404()
    return jsonify({'status': 'success', 'user': user.to_json()}), 200


@user.route('/create_user', methods=['POST'])
def create_user():
    post_data = request.get_json()
    
    #if username or email =0 ,raise error
    user = User(
        username = post_data.get('username'),
        email = post_data.get('email')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'User created'})


@user.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    post_data = request.get_json()
    user = User.query.filter_by(id=user_id).one_or_404()
    
    #add logic if only one is edited
    user.id = user_id
    user.username = post_data.get('username')
    user.email = post_data.get('email')
    
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'User updated'})


@user.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).one_or_404()

    db.session.delete(user)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'User deleted'})

