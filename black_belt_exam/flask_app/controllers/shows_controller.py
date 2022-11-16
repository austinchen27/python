from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.shows_model import Show

@app.route("/shows/new")
def new_show():
  return render_template("new.html")

@app.route("/shows")
def homepage():
  if "user_id" not in session:
    return("/")
  return redirect("/")

@app.route("/add_show", methods=["POST"])
def add_new_show():
  if "user_id" not in session:
    return("/")
  if not Show.validator(request.form):
    return redirect("/shows/new")
  show_data = {
    **request.form,
    "user_id": session["user_id"]
  }
  Show.create(show_data)
  return redirect("/dashboard")

@app.route("/shows/<int:id>")
def show_one(id): #pass id to class method from route <int:id>
  if "user_id" not in session:
    return("/")
  data = {
    "id": session["user_id"]
  }
  logged_user = User.get_by_id(data)
  this_show = Show.get_by_id({"id":id})
  my_likes = Show.select_all(data)
  count = Show.count_likes_by_show_id(id) #this is getting the count with the id
  return render_template("show_one.html", count=count, my_likes=my_likes, this_show=this_show, logged_user=logged_user)

@app.route("/shows/<int:id>/edit")
def edit_show(id):
  if "user_id" not in session:
    return("/")
  data = {
    "id": id
  }
  one_show = Show.get_by_id(data)
  return render_template("edit.html", one_show=one_show)

@app.route("/shows/<int:id>/update", methods=["POST"])
def update_show(id):
  if "user_id" not in session:
    return("/")
  if not Show.validator(request.form):
    return redirect(f"/show/{id}/edit")
  data = {
    "id":id,
    **request.form
  }
  Show.update(data)
  return redirect("/dashboard")

@app.route("/shows/<int:id>/delete")
def del_show(id):
  if "user_id" not in session:
    return redirect("/")
  data = {
    "id": id
  }
  this_show = Show.get_by_id(data)
  if not this_show.user_id == session["user_id"]: #person who is logged in
    flash("Hey, not yours, not gonna delete it")
    return redirect("/dashboard")
  Show.delete({"id":id})
  return redirect("/dashboard")

@app.route("/liked", methods=["POST"])
def like():
  data = {
    "user_id": session["user_id"],
    "show_id": request.form["quantity_id"]
  }
  Show.data_into_likes(data)
  return redirect("/dashboard")

@app.route("/unliked", methods=["POST"])
def unlike():
  data = {
    "user_id": session["user_id"],
    "show_id": request.form["quantity_id"]
  }
  Show.data_delete_likes(data)
  return redirect("/dashboard")

  # count how many user_id liked

    # session["quantity"] = 1
