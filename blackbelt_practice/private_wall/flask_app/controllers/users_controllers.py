from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_models import User
from flask_app.models.msg_models import Message

bcrypt = Bcrypt(app)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/users/register", methods=["POST"])
def user_reg():
  if not User.validator(request.form):
    return redirect("/")
  hashed_pass = bcrypt.generate_password_hash(request.form["password"])
  data = {
    **request.form,
    "password": hashed_pass
  }
  user_id = User.create(data)
  session["user_id"] = user_id
  return redirect("/dashboard")

@app.route("/dashboard")
def dash():
  if "user_id" not in session:
    return redirect("/")
  data = {
    "id": session["user_id"]
  }
  logged_user = User.get_by_id(data)
  return render_template("welcome.html", logged_user=logged_user)

@app.route("/users/logout")
def log_out():
  del session["user_id"]
  return redirect("/")

@app.route("/users/login", methods=["POST"])
def users_log():
  data = {
    "email": request.form["email"]
  }
  user_in_db = User.get_by_email(data)
  if not user_in_db:
    flash("Invalid credentials", "log")
    return redirect("/")
  if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
    flash("Invalid crednetials", "log")
    return redirect("/")
  session["user_id"] = user_in_db.id
  return redirect("/dashboard")

