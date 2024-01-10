from application import db
from datetime import datetime

class Post(db.Model):

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=False)
    caption = db.Column(db.String(256), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) 
    status = db.Column(db.Boolean, default=True)
    post_date      = db.Column(db.DateTime, default=datetime.utcnow) 
    comments = db.relationship("Comment", backref="commented", lazy=True)
    likes = db.relationship("Like", backref="liked", lazy=True)


class Comment(db.Model):

    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    commenter_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    text = db.Column(db.Text, nullable=False)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)
    hidden = db.Column(db.Boolean, default=False)


class Like(db.Model):

    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    status = db.Column(db.Boolean, default=True)
    like_date = db.Column(db.DateTime, default=datetime.utcnow)
