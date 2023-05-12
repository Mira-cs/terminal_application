import csv #importing files with quiz questions
from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingCirclesBar #to show how much progress user made through the quiz
import inquirer
import pyfiglet

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

literature = open("literature_questions.csv", "r")
datareader = csv.reader(literature)
headers = next(datareader)
literature_q = []
for row in datareader:
  for row in datareader:
      question_lit = {
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
      literature_q.append(row)
num_questions = len(questions) - 1
literature.close()

art = open("art_questions.csv", "r")
datareader = csv.reader(art)
headers = next(datareader)
art_q = []
for row in datareader:
        question_art = {
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
        art_q.append(row)
num_questions = len(questions) - 1
art.close()

count = 0
valid_options = ["a","b","c","d","A","B","C","D"]
no_question = 0
greeting = pyfiglet.figlet_format("Welcome to the Mutliple Choice Quiz!")

print(greeting)

while True:
    choose = input(cs("Choose from the topics available by typing movies, literature or art or anything else to exit:\n", "yellow")).lower()
    bar = FillingCirclesBar('Progress', max=num_questions)
    if choose == "movies":
        while no_question < num_questions:
            question = questions[no_question]
            prompt = inquirer.prompt([
                inquirer.List('choice',
                              message=question['message'],
                              choices=question['choices'],
                              ),
            ])
            answer = prompt['choice']
            if answer == questions[no_question]["correct_choice"]:
              count += 1
              no_question += 1
              bar.next(1)
              print(cs(f"\nGood job!You have {count} correct answer(s).\n", "green"))
            elif answer != questions[no_question]['correct_choice']:
              print(cs(f"\nWrong, you have {count} correct answer(s).\n", "red"))
              help = input(cs("Would you like a hint? (yes/no): \n","pink")).lower()
              if help == "yes":
                print(cs(questions[no_question]['hint'],"yellow"))
                if no_question < 1:
                  no_question = 0
              elif help != "yes":
                if no_question < 1:
                  no_question = 0
        no_question = 0
        count = 0
        del bar
    if choose == "literature":
      while no_question < num_questions:
            question_lit = literature_q[no_question]
            prompt = inquirer.prompt([
            inquirer.List('choice',
                              message=question_lit['message'],
                              choices=question_lit['choices'],
                              ),
            ])
            answer = prompt['choice']
            if answer == literature_q[no_question]["correct_choice"]:
              count += 1
              no_question += 1
              bar.next(1)
              print(cs(f"\nGood job!You have {count} correct answer(s).\n", "green"))
            elif answer != literature_q[no_question]['correct_choice']:
              print(cs(f"\nWrong, you have {count} correct answer(s).\n", "red"))
              help = input(cs("Would you like a hint? (yes/no): \n","pink")).lower()
              if help == "yes":
                print(cs(literature_q[no_question]['hint'],"yellow"))
                if no_question < 1:
                  no_question = 0
              elif help != "yes":
                if no_question < 1:
                  no_question = 0
      no_question = 0
      count = 0
      del bar

              

        
        
        
        
        
        
        


