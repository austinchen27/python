from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route("/recipes/new")
def create_page():
  return render_template("new.html")

@app.route("/add_recipe", methods=["POST"])
def new_recipe():
  if "user_id" not in session:
    return redirect("/")
  # if not Recipe.validator(request.form):
  #   return redirect("/recipe/new")
  data = {
    **request.form,
    "user_id": session["user_id"]
  }
  Recipe.create_recipe(data)
  return redirect("/recipes")

@app.route("/recipes/<int:id>")
def show_recipe(id):
  if "user_id" not in session:
    return redirect("/")
  data = {
    "id": session["user_id"]
  }
  return render_template("/view.html")




