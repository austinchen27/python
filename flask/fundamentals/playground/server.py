from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:times>')
@app.route('/play/<int:times>/<color>')
def index(times=3,color="#9EC5F8"):
  times = times
  color = color
  return render_template("index.html", times=times, color=color)



if __name__=="__main__":
  app.run(debug=True,port=5005)