from flask import Blueprint, jsonify, request
from website import db
from datetime import datetime
from .models import Post
import uuid

post = Blueprint('post', __name__)

@post.route('/posts', methods=['GET'])
def posts():
    if request.method == 'GET':
        posts = Post.query.order_by(Post.time).all()
        return jsonify({'status': 'success', 'posts': [post.to_json() for post in posts] })

@post.route('/posts/create', methods=['POST'])
def make_post():
    if request.method == 'POST':
        post_data = request.get_json()
        post = Post()

        post.id = uuid.uuid4().hex
        post.author = post_data.get('author')
        post.title = post_data.get('title')
        post.body = post_data.get('body')
        post.time = datetime.datetime.now()
        post.edited = False
        
        db.session.add(post)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Post added!'})

@post.route('/posts/edit/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
    if request.method == 'PUT':
        post_data = request.get_json()
        post = db.one_or_404(Post, id=post_id)

        post.body = post_data.get('body', post.body)
        post.time = datetime.datetime.now()       
        post.edited = True

        db.session.commit()
        
        return jsonify({'status': 'success', 'message': 'Post updated!'})

@post.route('/post/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    if request.method == 'DELETE':
        post = db.get_or_404(Post, id=post_id)

        db.session.delete(post)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Post deleted!'})

@post.route('/post/<int:post_id>', methods=['GET'])
def open_post(post_id):
    post = db.one_or_404(Post, id=post_id)
    return jsonify({'status': 'success', 'post': post.to_json()})