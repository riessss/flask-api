from datetime import datetime, timezone
from sqlalchemy import DateTime
import sqlalchemy.orm as so
import sqlalchemy as sa
from website import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True, unique=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    posts: so.Mapped[list['Post']] = so.relationship(back_populates='author')

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'posts': [post.to_json() for post in self.posts]
        }

    def __repr__(self):
        return "<Username {self.username} >."

    
class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(50))
    body: so.Mapped[str] = so.mapped_column(sa.String(250))
    time: so.Mapped[datetime] = so.mapped_column(DateTime(timezone=True),index=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    author: so.Mapped[User] = so.relationship(back_populates='posts')
    edited: so.Mapped[bool] = so.mapped_column(sa.Boolean())

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'time': self.time.isoformat() if self.time else None,
            'author': self.author.username,
            'edited': self.edited
            }

    def __repr__(self):
        return f"<Post(title='{self.title}', author='{self.author.username}')>"
