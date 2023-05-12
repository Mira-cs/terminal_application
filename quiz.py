import csv #importing files with quiz questions
from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingCirclesBar #to show how much progress user made through the quiz
import inquirer
import pyfiglet
from quiz_functions import user_input,quiz_progressbar
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
literature_allq = []
for row in datareader:
      literature_dict = {
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
      literature_allq.append(literature_dict)
num_questions = len(literature_allq) 
literature.close()

art = open("art_questions.csv", "r")
datareader = csv.reader(art)
headers = next(datareader)
art_allq = []
for row in datareader:
        art_dict = {
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
        art_allq.append(art_dict)
num_questions = len(art_allq) 
art.close()


count = 0
valid_options = ["movies","literature","art","exit"]
no_question = 0
greeting = pyfiglet.figlet_format("Welcome to the Mutliple Choice Quiz!", font ="digital")
bar = FillingCirclesBar('Progress', max=num_questions)
print(greeting)

while True:
      try:
        choose = user_input("Please choose one topic (movies,art or literature), or exit: ", "yellow")
        if choose not in valid_options:
          raise ValueError("Invalid answer")
        no_question = 0
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
                  quiz_progressbar(no_question)
                  print(cs(f"\nGood job!You have {count} correct answer(s) out of {no_question}\n", "green"))
              elif answer != questions[no_question]['correct_choice']:
                  print(cs(f"\nWrong, you have {count} correct answer(s).\n", "red"))
                  try: 
                    help = input(cs("Would you like a hint and try again? (yes/no): \n","pink")).lower()
                    if help not in ["yes","no"]:
                      raise ValueError(cs("Invalid Answer","red"))
                    if help == "yes":
                      print(cs(questions[no_question]['hint'],"yellow"))
                    elif help == "no":
                      no_question += 1
                  except ValueError as a:
                    print(a)
        if choose == "literature":
          while no_question < num_questions:
                literature_dict = literature_allq[no_question]
                prompt = inquirer.prompt([
                inquirer.List('choice',
                              message = literature_dict['message'],
                              choices = literature_dict['choices'],
                              ),
                ])
                answer= prompt['choice']
                if answer== literature_allq[no_question]["correct_choice"]:
                  count += 1
                  no_question += 1
                  quiz_progressbar(no_question)
                  print(cs(f"\nGood job!You have {count} correct answer(s).\n", "green"))
                elif answer != literature_allq[no_question]['correct_choice']:
                  print(cs(f"\nWrong, you have {count} correct answer(s).\n", "red"))
                  try:
                    help = input(cs("Would you like a hint and try again? (yes/no): \n","pink")).lower()
                    if help not in ["yes","no"]:
                      raise ValueError(cs("Invalid Answer","red"))
                    if help == "yes":
                      print(cs(literature_allq[no_question]['hint'],"yellow"))
                    elif help == "no":
                      no_question += 1
                  except ValueError as a:
                    print(a)
        elif choose == "art":
          while no_question < num_questions:
                art_dict = art_allq[no_question]
                prompt = inquirer.prompt([
                inquirer.List('choice',
                              message = art_dict['message'],
                              choices = art_dict['choices'],
                              ),
                ])
                answer= prompt['choice']
                if answer== art_allq[no_question]["correct_choice"]:
                  count += 1
                  no_question += 1
                  quiz_progressbar(no_question)
                  print(cs(f"\nGood job!You have {count} correct answer(s).\n", "green"))
                elif answer != art_allq[no_question]['correct_choice']:
                  print(cs(f"\nWrong, you have {count} correct answer(s).\n", "red"))
                  try:
                    help = input(cs("Would you like a hint and try again? (yes/no): \n","pink")).lower()
                    if help not in ["yes","no"]:
                        raise ValueError(cs("Invalid Answer","red"))
                    if help == "yes":
                      print(cs(art_allq[no_question]['hint'],"yellow"))
                    elif help == "no":
                      no_question += 1
                  except ValueError as a:
                    print(a)
        elif choose == "exit":
          break
        no_question = 0
        count = 0
        del bar
      except ValueError as e:
        print(e)
       
    
    
    
    

              

        
        
        
        
        
        
        

