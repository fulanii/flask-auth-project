

#**Flask imports
from flask import Flask


# Global varialbel?
app = Flask(__name__)
app.secret_key = "MY SUPER SECRET KEY"


#** import from my package
from social_app import routes 

