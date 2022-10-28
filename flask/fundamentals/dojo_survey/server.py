from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'chickenandrice' #secret key

@app.route('/')
def enter_site():
  return render_template("index.html")

@app.route('/result', methods=["POST"])
def result_page():
  session["name"] = request.form["name"]
  session["location"] = request.form["location"]
  session["language"] = request.form["language"]
  session["comments"] = request.form["comments"]
  return redirect('/result')

@app.route('/result')
def info():
  return render_template("result.html")

if __name__=="__main__":
  app.run(debug=True,port=5005)









