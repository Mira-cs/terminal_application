from quiz_functions import is_valid_input,quiz_progressbar
from progress.bar import FillingCirclesBar

# Testing to see if the program matches the input to the valid_options list items and returns the correct result
def test_is_valid_input(monkeypatch):
  # Mock user's input and set it to "movies"
  monkeypatch.setattr("builtins.input", lambda _: "movies")
  # Assert that "movies" is a valid input
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == True
  # Mock user's input and set it to "123"
  monkeypatch.setattr("builtins.input", lambda _: "123")
  # Assert that "movies" is an invalid input
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == False
  
  monkeypatch.setattr("builtins.input", lambda _: "art")
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == True

  monkeypatch.setattr("builtins.input", lambda _: "arts")
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == False
  
  monkeypatch.setattr("builtins.input", lambda _: "literature")
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == True

  monkeypatch.setattr("builtins.input", lambda _: "something")
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == False

#Testing if the progressbar works as expected
def test_quiz_progressbar():
    num_questions = 10
    bar = FillingCirclesBar("Progress", max=num_questions)
    # Testing that the bar is empty at the beginning
    assert bar.index == 0
    # Testing that the bar advances after calling next()
    bar.next()
    assert bar.index == 1
    # Testing that the bar is full after calling next() num_questions times
    for i in range(num_questions - 1):
        bar.next()
    assert bar.index == num_questions
  
