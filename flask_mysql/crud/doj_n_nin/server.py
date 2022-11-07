from flask_app.controllers import dojos_ctrl, ninjas_ctrl
from flask_app import app


if __name__ == "__main__":
  app.run(debug=True, port=5005)
