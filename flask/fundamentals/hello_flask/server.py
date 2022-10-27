from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/say/<word>/<int:times>')
def say_word(word,times):
    # return f"The word is {word,times}."
    return word * int(times)

@app.route('/template')
def template():
    return render_template("index.html", phrase="hello", times=5)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5005)    # Run the app in debug mode.

#pip install pipnv    <--- run this one ever so we can create virtual environments
#pipenv install flask    <--- run this once PER PROJECT to set up a ve
#exit    <--- Leave ve

#pipenv install flask
#pipenv shell
#python3 server.py

