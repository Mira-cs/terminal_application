from quiz_functions import user_input
from stringcolor import cs
def test_user_input(monkeypatch):
  monkeypatch.setattr("builtins.input",lambda _:"movies")
  assert user_input("Please choose one topic (movies,art or literature), or exit: ","yellow") == "movies"
  