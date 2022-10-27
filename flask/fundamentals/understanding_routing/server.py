from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# #1. localhost:5000/ - have it say "Hello World!"

# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


# #2. localhost:5000/dojo - have it say "Dojo!"

# @app.route('/dojo')
# def dojo():
#     return 'Dojo!'


# #3. Create one url pattern and function that can handle the following examples:

# @app.route('/say/<word>')
# def say_word(word):
#     return f"Hi {word}!"


# #4. Create one url pattern and function that can handle the following 
# examples (HINT: int() will come in handy! For example int("35") returns 35):

# @app.route('/repeat/<int:times>/<word>')
# def repeat(word,times):
#     # return f"The word is {word,times}."
#     return word * int(times)



# // reference: template
# @app.route('/template')
# def template():
#     return render_template("index.html", phrase="hello", times=5)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5005)    # Run the app in debug mode.
