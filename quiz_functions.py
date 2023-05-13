from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingCirclesBar #to show how much progress user made through the quiz
import csv

movies = open("movie_questions.csv", "r")
datareader = csv.reader(movies)
headers = next(datareader)
questions = []
for row in datareader:
      question = {
            'message': row[0],
            'choices': [
                row[1],
                row[2],
                row[3],
                row[4]
            ],
            'correct_choice': row [5],
            'hint': row[6]
        }
      questions.append(question)
num_questions = len(questions) 
movies.close()

#function used in the app to take users input(choosing a topic)
def user_input(topics,color):
  choose = input(cs(topics,color)).lower()
  return choose
 
#function used for testing purposes
def is_valid_input(message,color):
  # Storing the user input in the variable "text"
  text = input(cs(message,color)).lower()
  # Storing list of items in the variable "valid_options"
  valid_options = ["movies", "literature", "art", "exit"]
  # Iterating through the list and storing each item in the option variable
  for option in valid_options:
    # If the input is equal to the item stored in option variable, return True, else, return False
    if text == option:
      return True
  return False

# Function made for the progress bar
def quiz_progressbar(no_question):
  # Passing two instance into the class FillinCirclesBar, text "Progress" and length  
  bar = FillingCirclesBar("Progress",max = num_questions)
  # If statement, which makes bar progress if the current question number is less than the total
  if no_question <=  num_questions:
    # Bar will progress by the number of the current question
    bar.next(no_question)



  



  