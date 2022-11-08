from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask import Bcrypt -----**
from flask_app.models.user_model import User
from flask_app.models.party_model import Party






@app.route("/dsashboard")
def dash():
  if "user_id" not in session:
    return redirect("/")
  data = {
    "id":session["user_id"]
  }
  logged_user = User.get_by_id(data)
  all_parties = Party.get_all()
  return render_template("welcome.html, logged_user=logged_user, all_parties=all_parties")

