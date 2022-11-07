from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.userlogin import User

bcrypt = Bcrypt(app)

@app.route("/")
def index():
  return render_template("index.html")