import csv #importing files with quiz questions
from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingCirclesBar #to show how much progress user made through the quiz

def qalist_movies(i, questions):
  print("\nQuestion ",i , "-", questions[i][0])
  print("A", questions[i][1])
  print("B ", questions[i][2])
  print("C ", questions[i][3])
  print("D ", questions[i][4])
def qalist_literature(i, literature_q):
  print("\nQuestion ", i , "-", literature_q[i][0])
  print("A", literature_q[i][1])
  print("B ", literature_q[i][2])
  print("C ", literature_q[i][3])
  print("D ", literature_q[i][4])
def qalist_art(i,art_q):
  print("\nQuestion ", i , "-", art_q[i][0])
  print("A", art_q[i][1])
  print("B ", art_q[i][2])
  print("C ", art_q[i][3])
  print("D ", art_q[i][4])
def help():
  help = input(cs("Would you like a hint? (yes/no): \n","pink")).lower()
  if help == "yes":
    print(cs(questions[no_question]['hint'],"yellow"))
    if no_question < 1:
      no_question = 0
    elif help != "yes":
      if no_question < 1:
        no_question = 0

  