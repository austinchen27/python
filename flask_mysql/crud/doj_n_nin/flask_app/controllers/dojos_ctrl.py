from flask_app.models.dojos_tbl import Dojo
from flask import render_template, redirect, request, session, flash
from flask_app import app

@app.route("/")
def index():
  dojos = Dojo.get_all()
  return render_template("dojos.html", dojos = dojos)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
  data = {
    "name": request.form["name"]
  }
  Dojo.save(data)
  return redirect("/")

@app.route("/dojos/<int:id>")
def dojo_show(id):
  data = {
    "id":id
  }
  dojoName = Dojo.get_one(data)
  return render_template("dojoshow.html", dojoName = dojoName)




#.without() Attribute
#.() class method


#sendingback 1 dog with all award
#1 dojo w all ninjas stored into an attribute of that dojo instance