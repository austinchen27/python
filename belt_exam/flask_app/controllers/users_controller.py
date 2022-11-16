from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.painting_model import Painting

bcrypt = Bcrypt(app)

@app.route("/")
def index():
  if "user_id" in session: #below*
    return redirect("/dashboard") #somebody is logged in, so send them to dashboard
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
    flash("Invalid credentials", "log")
    return redirect("/")
  session["user_id"] = user_in_db.id
  return redirect("/dashboard")

@app.route("/users/logout")
def log_out():
  del session["user_id"]
  # session.clear()
  # session.pop("user_id")
  return redirect("/")

@app.route("/dashboard")
def dash():
  if "user_id" not in session: #user should have to login to view the page, this line and next line
    return redirect("/") #they're not logged in, don't let them see this route and send them back to the login
  data = {
    "id": session["user_id"]
  }
  logged_user = User.get_by_id(data)
  all_paintings = Painting.get_all()
  my_purchases = Painting.select_all(data)
  return render_template("welcome.html", logged_user=logged_user, all_paintings=all_paintings, my_purchases=my_purchases)
#ON dashboard page so function is here -> this is where you show your purchases jinja

@app.route("/paintings/<int:id>/update", methods=["POST"])
def update_painting(id):
  if "user_id" not in session:
    return("/")
  if not Painting.validator(request.form):
    return redirect(f"/paintings/{id}/edit")
  data = {
    "id":id,
    **request.form
  }
  Painting.update(data)
  return redirect("/dashboard")