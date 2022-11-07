from flask import flask
app = Flask(__name__)
app.secret_key = "no sec"
DATABASE = 'nov_parties'