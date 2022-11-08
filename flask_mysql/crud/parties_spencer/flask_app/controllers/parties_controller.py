from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.party_model import Party

@app.route("/parties/new")
def new_party():
  return render_template("party_new.html")

@app.route("/parties/create", methods=["POST"])
def create_party():
  if "user_id" not in session:
    return("/")
  if not Party.validator(request.form):
    return redirect("/parties/new")
  party_data = {
    **request.form,
    "user_id": session["user_id"]
  }
  Party.create(party_data)
  return redirect("/dsashboard")

@app.route("/parties/<int:id>/edit")
def edit_user_form(id):
  if "user_id" not in session:
    return("/")
  data = {
    "id": id
  }
  one_party = Party.get_by_id(data)
  return render_template("party_edit.html", one_party=one_party)

@app.route("/parties/<int:id>/update", methods=["POST"])
def update_user(id):
  if "user_id" not in session:
    return("/")
  if not Party.validator(request.form):
    return redirect("/parties/{id}/edit")

  data = {
    "id": id,
    **request.form
  }
  Party.update(data)
  return redirect("/dashboard")