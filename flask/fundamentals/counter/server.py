from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'chickenandrice' #secret key

@app.route('/')
def enter_site():
  if "num" in session:
    session["num"] += 1
  else:
    session["num"] = 1
  return render_template("index.html", num=session["num"])

@app.route('/count')
def add_count():
  session["num"] += 1
  return redirect('/')

@app.route('/reset')
def reset_count():
  session["num"] = 0
  return redirect('/')



if __name__=="__main__":
  app.run(debug=True,port=5005)