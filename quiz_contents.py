import csv 
from stringcolor import cs

movies = open("movie_questions.csv", "r")
datareader = csv.reader(movies)
questions = []
for row in datareader:
  questions.append(row)
num_questions = len(questions) -1
movies.close()

literature = open("literature_questions.csv", "r")
datareader = csv.reader(literature)
literature_q = []
for row in datareader:
  literature_q.append(row)
num_questions_literature = len(literature_q) -1
literature.close()

print(cs("Hello! Welcome to the Multiple Choice Quiz!","blue"))
choose = input(cs("Please choose a topic for the quiz (movie or literature): ","orchid")).lower()

