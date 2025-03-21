from datetime import datetime, timezone
from sqlalchemy import DateTime
import sqlalchemy.orm as so
import sqlalchemy as sa
from app import db

class User(db.Model):
    __tablename__ = "user_table"
    id: so.Mapped[int] = so.mapped_column(primary_key=True, unique=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    password: so.Mapped[str] = so.mapped_column(sa.String(150))
    posts: so.Mapped['Post'] = so.relationship(back_populates="author")

    def __rper__(self):
        pass

    
class Post(db.Model):
    __tablename__ = "post_table"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.WriteOnlyCollection[str] = so.mapped_column(sa.String(250))
    time: so.Mapped[datetime] = so.mapped_column(DateTime(timezone=True))
    author: so.Mapped[str] = so.relationship(back_populates=User.id)

    def __repr(self):
        pass
