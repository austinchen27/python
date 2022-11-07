from flask_app.models.ninjas_tbl import Ninja
from flask_app.models.dojos_tbl import Dojo
from flask import render_template, redirect, request, session, flash
from flask_app import app

# goes to add ninja page
@app.route("/add_ninja")
def add_ninja():
  all_dojos = Dojo.get_all()
  print(all_dojos)
  return render_template("ninjas.html", dojos = all_dojos)


#input data into ninja field, then redirects it to
# all dojos box 
@app.route("/create_ninja", methods=["POST"])
def create_ninja():
  data = {
    "dojo_id": request.form["dojos"],
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "age": request.form["age"]
  }
  Ninja.new_ninja(data)
  return redirect("/dojos_box")

@app.route("/dojos_box")
def dojo_box():
  all_dojos = Dojo.get_all()
  # print(all_dojos[0].name)
  return render_template("dojos_show.html", dojo = all_dojos)

#dojo = all_dojos
#left side = jinja html
#right side = information

# for x in range([50,50,50]);
# print([0])

#this route will take you to the page that shows
#each ninjas in the dojo
@app.route("/ninjas/<int:id>")
def ninjas_in_dojo():
  data = {
    "id":id
  }
  ninjas = Ninja.all_ninjas(data)
  return render_template("/dojos_show.html", )

