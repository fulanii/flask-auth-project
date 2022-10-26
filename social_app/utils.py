

# Flask imports 
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import  current_user


# Imports from my package
from social_app.db_models import User, db1, Post, db2


def add_user_to_db(data:dict):
    email = data["email"]
    username = data["username"]
    password = data["password"]

    try:
        password_hash =  generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(username=username, password=password_hash, email=email)
        db1.session.add(new_user)
        db1.session.commit()
        return True
    except Exception as err:
        return False


def add_to_post_db(data):
    new_post = Post(username=current_user.username, post=data["post-text"])
    try:
        post = data["post-text"]
        if post == " ":
            return False
        else:
            new_post = Post(username=current_user.username, post=post)
            db2.session.add(new_post)
            db2.session.commit()
            return True
    except Exception as err:
        print(err)
        return False


def get_all_posts():
   all_posts = Post.query.all()
   return all_posts


def delete_posts(id:int) -> bool:
    
    return True
