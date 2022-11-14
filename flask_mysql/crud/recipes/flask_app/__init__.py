from flask import Flask
app = Flask(__name__)
app.secret_key = "ch1ck3nandr1c3"
DATABASE = "recipes"