

# Flask imports 
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy

# Imports from my package
from social_app.db_models import User, db1


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
