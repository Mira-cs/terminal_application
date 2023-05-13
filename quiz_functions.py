from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingCirclesBar #to show how much progress user made through the quiz
import csv
import inquirer
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
  text = input(cs(message,color)).lower()
  valid_options = ["movies", "literature", "art", "exit"]
  for option in valid_options:
    if text == option:
      return True
  return False

def quiz_progressbar(no_question):
  bar = FillingCirclesBar("Progress",max = num_questions)
  if no_question <=  num_questions:
    bar.next(no_question)



  



  