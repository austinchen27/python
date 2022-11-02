from flask import Flask, render_template, request, redirect
from models.users import User
app = Flask(__name__)

@app.route("/")
def index():
  users = User.get_all()
  print(users)
  return render_template("readall.html", users=users)

@app.route("/dashboard")
def dashboard():
  return render_template("create_user.html")

@app.route("/create_user", methods=["POST"])
def create_user():
  data = {
    "fname": request.form["fname"],
    "lname": request.form["lname"],
    "email": request.form["email"]
  }

  User.save(data)
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True, port=5005)



#dont put .html in url, only in render_template