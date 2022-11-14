from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

@app.route("/recipes/new")
def create_recipe_page():
  return render_template("new.html")

@app.route("/recipes")
def homepage():
  if "user_id" not in session:
    return("/")
  return redirect("/")

@app.route("/add_recipe", methods=["POST"])
def add_new_recipe():
  if "user_id" not in session: #if user not logged in, no access
    return("/")
  if not Recipe.validator(request.form): #check validator with form info
    return redirect("/recipes/new")
  recipe_data = {
    **request.form,
    "user_id": session["user_id"]
  }
  Recipe.create(recipe_data)
  return redirect("/dashboard")

# @app.route("/{name}")
# def show_one_recipe_redirect():
#   data = {
#     "id": session["user_id"]
#   }
#   return redirect("f/recipes/{id}")

@app.route("/recipes/<int:id>")
def show_one_recipe(id):
  if "user_id" not in session:
    return("/")
  data = {
    "id": session["user_id"]
  }
  logged_user = User.get_by_id(data)
  this_recipe = Recipe.get_by_id({"id":id})
  return render_template("my_recipes.html", this_recipe=this_recipe, logged_user=logged_user)

@app.route("/recipes/<int:id>/edit")
def edit_user_form(id):
  if "user_id" not in session:
    return("/")
  data = {
    "id": id #id is the id from our pathway (int:id)
  }
  one_recipe = Recipe.get_by_id(data) #pass data so we are getting the id
  return render_template("edit.html", one_recipe=one_recipe) #pass one_party for editing

@app.route("/recipes/<int:id>/update", methods=["POST"])
def update_user(id):
  if "user_id" not in session:
    return("/")
  if not Recipe.validator(request.form):
    return redirect(f"/recipes/{id}/edit")
  data = {
    "id":id,
    **request.form
  }
  Recipe.update(data)
  return redirect("/dashboard")

@app.route("/recipes/<int:id>/delete")
def del_party(id):
  if "user_id" not in session:
    return redirect("/")
  data = {
    "id": id
  }
  this_recipe = Recipe.get_by_id(data)
  if not this_recipe.user_id == session["user_id"]: #person who is logged in
    flash("Hey, not yours, not gonna delete it")
    return redirect("/dashboard")
  Recipe.delete({"id":id})
  return redirect("/dashboard")