kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

class Player:

  def __init__(self, info):
    self.name = info["name"]
    self.age = info["age"]
    self.position = info["position"]
    self.team = info["team"]

  def __repr__(self):
    display = f"{self.name} is {self.age} years old, is {self.position} playing for the {self.team}"
    return display

player1 = Player(kevin)
player2 = Player(jason)
player3 = Player(kyrie)
print(player1)
print(player2)
print(player3)