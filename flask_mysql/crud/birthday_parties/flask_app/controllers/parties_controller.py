from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.party_model import Party

@app.route("/parties/new")
def new_party():
  return render_template("party_new.html")

@app.route("/parties/create", methods=["POST"]) #process route
def create_party():
  if "user_id" not in session: #if user not logged in, no access
    return("/")
  if not Party.validator(request.form): #check validator with form info
    return redirect("/parties/new")
  party_data = {
    **request.form,
    "user_id": session["user_id"]
  }
  Party.create(party_data)
  return redirect("/dashboard")

@app.route("/parties/<int:id>")
def show_one_party(id):
  if "user_id" not in session:
    return("/")
  this_party = Party.get_by_id({"id":id})
  return render_template("party_one.html", this_party=this_party)

@app.route("/my_parties")
def show_parties_for_logged_user(): #creating function for SHOW page 
  if "user_id" not in session:
    return("/")
  logged_user = User.get_by_id({"id":session["user_id"]})
  return render_template("my_parties.html", logged_user=logged_user)

@app.route("/parties/<int:id>/edit")
def edit_user_form(id):
  if "user_id" not in session:
    return("/")
  data = {
    "id": id #id is the id from our pathway (int:id)
  }
  one_party = Party.get_by_id(data) #pass data so we are getting the id
  return render_template("party_edit.html", one_party=one_party) #pass one_party for editing

@app.route("/parties/<int:id>/update", methods=["POST"])
def update_user(id):
  if "user_id" not in session:
    return("/")
  if not Party.validator(request.form):
    return redirect(f"/parties/{id}/edit")
  data = {
    "id":id,
    **request.form
  }
  Party.update(data)
  return redirect("/dashboard")

@app.route("/parties/<int:id>/delete")
def del_party(id):
  if "user_id" not in session:
    return redirect("/")
  data = {
    "id": id
  }
  this_party = Party.get_by_id(data)
  if not this_party.user_id == session["user_id"]: #person who is logged in
    flash("Hey, not yours, not gonna delete it")
    return redirect("/dashboard")
  Party.delete({"id":id})
  return redirect("/dashboard")