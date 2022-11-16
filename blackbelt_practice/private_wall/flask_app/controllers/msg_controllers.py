from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_models import User
from flask_app.models.msg_models import Message

@app.route("/create_message", methods=["POST"])
def new_message():
  # if "user_id" not in session:
  #   return render_template("test.html")
  # if not Message.validator_msg(request.form):
  #   return redirect("/dashboard")
  msg_data = {
    **request.form,
    "user_id": session["user_id"]
  }
  Message.create_message(msg_data)
  return redirect("/msg_wall")

@app.route("/msg_wall")
def display_messages():
  if "user_id" not in session:
    return("/")
  data = {
    "id": session["user_id"]
  }
  logged_user = User.get_by_id(data)
  this_message = Message.get_by_id({"id":session["user_id"]})
  return render_template("welcome.html", this_message=this_message, logged_user=logged_user)