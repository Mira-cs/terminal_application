from quiz_functions import is_valid_input
from progress.bar import FillingCirclesBar
# testing to see if the program matches the input to the valid_options list items and returns the correct result
def test_is_valid_input(monkeypatch):
  monkeypatch.setattr("builtins.input", lambda _: "movies")
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == True

  monkeypatch.setattr("builtins.input", lambda _: "invalid")
  assert is_valid_input("Please choose one topic (movies, art, literature, or exit): ", "yellow") == False
def test_quiz_progress_bar():
    num_questions = 5
    bar = FillingCirclesBar('Progress', max=num_questions - 1)
    for i in range(num_questions):
        # Simulate answering a question
        bar.next(1)
    bar.finish()
    assert bar.index == num_questions - 1 
  
