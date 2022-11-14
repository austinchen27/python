from flask_app.controllers.users_controller import User
from flask_app.controllers.recipes_controller import Recipe
from flask_app import app


if __name__ == "__main__":
  app.run(debug=True, port=5005)
