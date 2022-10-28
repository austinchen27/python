from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/form') #VIEW
def display_form():
    return render_template("form.html")

@app.route('/food_form_process', methods=['POST']) #ACTION  - NEVER RENDER ON AN ACTION ROUTE (refresh issue)
def process_form():
    print(request.form)
    session['food_name'] = request.form['name']
    session['spicy'] = request.form['is_spicy']
    if 'check' in request.form:
        session['check'] = request.form['check']
    # return "test"
    # return render_template("index.html", food_name=request.form["name"], spicy=request.form["is_spicy"]) #this is bad practice
    return redirect('/show')

@app.route('/show')
def show():
    # if "food_name" not in session:
        # return redirect('/form')
    return render_template("show.html")
    # return render_template("show.html", food_name=request.form['name'], spicy=request.form['is_spicy'])

if __name__ == "__main__":
    app.run(debug=True,port=5005)

