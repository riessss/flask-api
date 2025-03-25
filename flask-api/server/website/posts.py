from flask import Blueprint, jsonify, request
from website import db
from datetime import datetime
from .models import Post
import uuid

post = Blueprint('post', __name__)

@post.route('/', methods=['GET'])
def posts():
    if request.method == 'GET':
        posts = Post.query.order_by(Post.time).all()
        return jsonify({'status': 'success', 'posts': [post.to_json() for post in posts] })

@post.route('/<int:post_id>', methods=['GET'])
def open_post(post_id):
    post = Post.query.filter_by(id=post_id).one_or_404()
    return jsonify({'status': 'success', 'post': post.to_json()})

@post.route('/create/<int:user_id>', methods=['POST'])
def make_post(user_id):
    if request.method == 'POST':
        post_data = request.get_json()
        post = Post(
            user_id = user_id,
            title = post_data.get('title'),
            body = post_data.get('body'),
            time = datetime.now(),
            edited = False
        )
        db.session.add(post)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Post added!'})

@post.route('/edit/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
    if request.method == 'PUT':
        post_data = request.get_json()
        post = Post.query.filter_by(id=post_id).one_or_404()

        post.body = post_data.get('body', post.body)
        post.time = datetime.now()       
        post.edited = True

        db.session.commit()
        
        return jsonify({'status': 'success', 'message': 'Post updated!'})

@post.route('/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    if request.method == 'DELETE':
        post = Post.query.filter_by(id=post_id).one_or_404()

        db.session.delete(post)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Post deleted!'})
