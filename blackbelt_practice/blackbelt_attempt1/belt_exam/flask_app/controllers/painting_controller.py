from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.painting_model import Painting

@app.route("/paintings/new")
def new_painting():
  return render_template("paintings_new.html")

@app.route("/paintings")
def homepage():
  if "user_id" not in session:
    return("/")
  return redirect("/")

@app.route("/add_painting", methods=["POST"])
def add_new_painting():
  if "user_id" not in session: #if user not logged in, no access
    return("/")
  if not Painting.validator(request.form): #check validator with form info
    return redirect("/paintings/new")
  painting_data = {
    **request.form,
    "user_id": session["user_id"]
  }
  Painting.create(painting_data)
  return redirect("/dashboard")

@app.route("/paintings/<int:id>/edit")
def edit_user_form(id):
  if "user_id" not in session:
    return("/")
  data = {
    "id": id #id is the id from our pathway (int:id)
  }
  one_painting = Painting.get_by_id(data) #pass data so we are getting the id
  return render_template("paintings_edit.html", one_painting=one_painting) #pass one_painting for editing

@app.route("/paintings/<int:id>/update", methods=["POST"])
def update_user(id):
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

@app.route("/paintings/<int:id>")
def show_one_painting(id):
  if "user_id" not in session:
    return("/")
  data = {
    "id": session["user_id"]
  }
  logged_user = User.get_by_id(data)
  this_painting = Painting.get_by_id({"id":id})
  return render_template("paintings_one.html", this_painting=this_painting, logged_user=logged_user)

@app.route("/paintings/<int:id>/delete")
def del_party(id):
  if "user_id" not in session:
    return redirect("/")
  data = {
    "id": id
  }
  this_painting = Painting.get_by_id(data)
  if not this_painting.user_id == session["user_id"]: #person who is logged in
    flash("Hey, not yours, not gonna delete it")
    return redirect("/dashboard")
  Painting.delete({"id":id})
  return redirect("/dashboard")