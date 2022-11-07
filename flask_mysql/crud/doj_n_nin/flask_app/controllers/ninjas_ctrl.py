from flask_app.models.ninjas_tbl import Ninja
from flask_app.models.dojos_tbl import Dojo
from flask import render_template, redirect, request, session, flash
from flask_app import app

@app.route("/add_ninja")
def add_ninja():
  all_dojos = Dojo.get_all()
  print(all_dojos)
  return render_template("ninjas.html", dojos = all_dojos)

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
  data = {
    "dojo_id": request.form["dojos"],
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "age": request.form["age"]
  }
  ninja_id = (data["dojo_id"])
  Ninja.new_ninja(data)
  return redirect(f"/dojos/{ninja_id}")


@app.route("/dojos/<int:id>")
def all_ninjas_in_dojos(id):
  data = {
    "id":id
  }
  ninjas = Ninja.all_ninjas(data)
  return render_template("dojoshow.html", ninjas = ninjas)


@app.route("/home")
def home():
  return redirect("/dojos")

@app.route("/dojos")
def dashboard():
  dojos = Dojo.get_all()
  return render_template("dojos.html", dojos = dojos)

  #f strings only in redirect, not in route