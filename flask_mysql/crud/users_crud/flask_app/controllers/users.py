from flask_app.models.user import User
from flask import render_template,redirect,request,session,flash
from flask_app import app


@app.route("/")
def index():
  users = User.get_all()
  print(users)
  return render_template("readall.html", users = users)


@app.route("/dashboard")
def dashboard():
  return render_template("create_user.html")


@app.route("/create_user", methods=["POST"])
def create_user():
  data = {
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "email": request.form["email"]
  }

  User.save(data)
  return redirect("/")


@app.route("/show/<int:id>")
def show(id):
  data = {
    "id":id
  }
  return render_template("readone.html", one_user = User.get_one(data))


@app.route("/edit/<int:id>")
def edit(id):
  data = {
    "id":id
  }
  return render_template("readedit.html", users = User.get_one(data))


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
  data = {
    **request.form, "id":id
  }
  User.update(data)
  return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
  data = {
    "id":id
  }
  User.delete(data)
  return redirect("/")


