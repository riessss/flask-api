from flask import Blueprint, jsonify
from website import db
from models import Post

post = Blueprint('post', __name__)

@post.route('/posts', methods=['GET'])
def posts():
    'hgdh'
    return jsonify()

@post.route()
def open_post():
    pass

@post.route()
def make_post():
    post = Post(
        #create_post
    )
    pass

@post.route()
def edit_post():
    pass

@post.route()
def delete_post():
    pass