

# Flask Imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# Imports From My Package
from social_app import app

# This module variables
db1 = SQLAlchemy()
db2 = SQLAlchemy()


SQLALCHEMY_DATABASE_URI = "sqlite:///database/User.db"
app.config['SQLALCHEMY_BINDS']= {
    'db1': SQLALCHEMY_DATABASE_URI,
    'db2': "sqlite:///database/Post.db"
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db1.init_app(app)
db2.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db1.Model):
    __bind_key__ = "db1"

    id = db1.Column(db1.Integer, primary_key=True)
    username = db1.Column(db1.String(30), unique=True, nullable=False)
    password = db1.Column(db1.String,  unique=False, nullable=False)
    email = db1.Column(db1.String,  unique=True, nullable=False)
    info = {'bind_key': 'db1'}

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False


class Post(db2.Model):
    __bind_key__= "db2"

    id = db2.Column(db2.Integer, primary_key=True)
    username = db2.Column(db2.String(30), nullable=False, unique=False )
    post = db2.Column(db2.String(250), nullable=False, unique=False)
    info = {'bind_key': 'db2'}





#** Run only once when creating db
# with app.app_context():
#     db1.create_all(bind=['db1'])
#     db2.create_all(bind=['db2'])


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
