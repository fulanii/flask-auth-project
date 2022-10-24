

# Flask Imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# Imports From My Package
from social_app import app

# This module variables
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/User.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String,  unique=False, nullable=False)
    email = db.Column(db.String,  unique=True, nullable=False)

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False




#** Run only once when creating db
# with app.app_context():
#     db.create_all().

#** Inserting in db
# me = User(username='asdfa',password='343434' ,email='szcxzc@example.com')
# db.session.add(me)
# db.session.commit()

#** working in cli 
# >>> from social_app import User, app
# >>> with app.app_context():
# ...     x = User.query.filter_by(id=1).first()
# ... 
# >>> print(x) output: <User 1>
# >>> print(x.email) output: dadaemail@g.com
