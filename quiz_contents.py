import csv #importing files with quiz questions
from stringcolor import cs #importing one module from stringcolor, to change the color of text
import random #to be able to generate random question from chosen topic

movies = open("movie_questions.csv", "r")
datareader = csv.reader(movies)
questions = []
for row in datareader:
  questions.append(row)
num_questions = len(questions) - 1
movies.close()

literature = open("literature_questions.csv", "r")
datareader = csv.reader(literature)
literature_q = []
for row in datareader:
  literature_q.append(row)
num_questions_literature = len(literature_q) - 1
literature.close()

art = open("art_questions.csv", "r")
datareader = csv.reader(art)
art_q = []
for row in datareader:
  art_q.append(row)
num_questions_art = len(art_q) - 1
art.close()

#  Outputs a welcome message and lets the user decide the topic
print(cs("Hello! Welcome to the Multiple Choice Quiz!","blue"))
count = 0
valid_options = ["a","b","c","d","A","B","C","D"]
q_number = 1
while True:
  choose = input(cs("\nChoose from the topics available by typing movies,literature or art and anything else to exit: \n","orchid")).lower()
  while choose == "movies" or choose == "literature" or choose == "art":
    if choose == "movies":
      for i in range(1,10):
            print("Question ", i , "-", questions[q_number][0])
            print("A", questions[q_number][1])
            print("B ", questions[q_number][2])
            print("C ", questions[q_number][3])
            print("D ", questions[q_number][4])
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == questions[q_number][5]:
              count += 1
              print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
              q_number += 1
            elif answer in valid_options:
              print(cs(f"\n Wrong,you have {count} correct answer(s)\n", "red"))
              q_number += 1 
            else:
              print(cs("Please provide a valid answer","yellow"))
              break
    elif choose == "literature":
        for i in range(1,10):
            print("Question ", i , "-", literature_q[q_number][0])
            print("A", literature_q[q_number][1])
            print("B ", literature_q[q_number][2])
            print("C ", literature_q[q_number][3])
            print("D ", literature_q[q_number][4])
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == literature_q[q_number][5]:
              count += 1
              print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
              q_number += 1
            elif answer in valid_options:
              print(cs(f"\n Wrong,you have {count} correct answer(s)\n", "red"))
              q_number += 1 
            else:
              print(cs("Please provide a valid answer","yellow"))
              break
    elif choose == "art":
        for i in range(1,10):
            print("Question ", i , "-", art_q[i][0])
            print("A", art_q[i][1])
            print("B ", art_q[i][2])
            print("C ", art_q[i][3])
            print("D ", art_q[i][4])
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == art_q[i][5]:
              count += 1
              print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
            elif answer in valid_options:
              print(cs(f"\n Wrong,you have {count} correct answer(s)\n", "red"))
            else:
              print(cs("Please provide a valid answer","yellow"))
              break
    if count >= 8:
      print(cs(f"\nWow,good job, you have {count} correct answer(s) out of {i} questions!\n", "purple"))
      yes_no = input("Would you like to take quiz again?: ")
      if yes_no == "yes":
        continue
      else:
        break
    elif count <= 7:
      print(cs(f"\nYou have {count} correct answer(s) out of {i}.Don't worry, you can always play again!\n", "purple"))
      yes_no = input("Would you like to take quiz again?: ")
      if yes_no == "yes":
        continue
      else:
        break
  else:
    print(cs("\nPlease provide a valid answer\n","yellow"))
    break
