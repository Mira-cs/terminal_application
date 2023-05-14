# Importing files with quiz questions
import csv 
# Importing one module from stringcolor, to change the color of text
from stringcolor import cs 
# Module to show how much progress user made through the quiz
from progress.bar import FillingCirclesBar 
# Inquirer package styles the quiz app 
import inquirer
# Importing pyfiglet to insert ASCII aty
import pyfiglet
# Importing two functions from quiz_functions file
from quiz_functions import user_input,quiz_progressbar,yes_no

# Opening file "movie_questions" and iterating over it,creating a list with dictionaries (key/value pairs)
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
      'correct_choice': row[5],
      'hint': row[6]
    }
    questions.append(question)
num_questions = len(questions)
movies.close()
# Opening file "literature_questions" and iterating over it,creating a list with dictionaries (key/value pairs)
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
# Opening file "art_questions" and iterating over it,creating a list with dictionaries (key/value pairs)
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
# Declaring variables 
count = 0
valid_options = ["movies", "literature", "art", "exit"]
no_question = 0
# Storing the greeting message (styled with pyfiglet package) in the variable "greeting"
greeting = pyfiglet.figlet_format("Welcome to the Mutliple Choice Quiz!", font = "digital")
goodbye = pyfiglet.figlet_format("Thank you!", font = "digital")
# Start of the app with greeting
print(greeting)
# While true loop will keep executing unless the user wishes to "exit"
while True:
    # Try/except statement for the invalid user input, to show the Error message in case it happens
    try:
        # Prompts user to input the topic they would like to take quiz about, color of the prompt yellow
        choose = user_input("\nPlease choose one topic (movies, art or literature), or exit: ", "yellow")
        # If input is invalid, show the error message
        if choose not in valid_options:
          raise ValueError("Invalid answer")
        # If user chooses "movies" topic, do this
        if choose == "movies":
          # While the current question is less than the total number of questions, keep executing
          while no_question < num_questions:
              # Assigning the question variable the value from the list, displaying the question with the "no_question" index      
              question = questions[no_question]
              # Displaying the question with the choices available and waits for user to choose one
              prompt = inquirer.prompt([
                      inquirer.List(
                                  'choice',
                                  message = question['message'],
                                  choices = question['choices'],
                                  ),
              ])
              # Assigning the answer variable the choice user makes
              answer = prompt['choice']
              # If statement checks if the answer matches the correct answer
              if answer == questions[no_question]["correct_choice"]:
                  # If yes, the score increases as well as the number of the question 
                  count += 1
                  no_question += 1
                  # Progress Bar goes up with the increase of the number of the question
                  quiz_progressbar(no_question,num_questions)
                  # Outputting the message in the terminal, as well as the number of correct answers, in color green
                  print(cs(f"\nGood job!You have {count} correct answer(s) out of {no_question}.\n", "green"))
              # If answer doesnt match the correct one, print "Wrong" message
              elif answer != questions[no_question]['correct_choice']:
                  quiz_progressbar(no_question,num_questions)
                  print(cs(f"\nWrong, you have {count} correct answer(s) out of {no_question}.\n", "red"))
                  # Try/except block to display an Error message in case of invalid input
                  try: 
                    help = yes_no("\nWould you like a hint and try again? (yes/no): ","pink")
                    # If user requests a hint, program will output it and go back to the question
                    if help == "yes":
                      print(cs(questions[no_question]['hint'], "yellow"))
                    # If user says no the hint, the program will move on to the next question
                    elif help == "no":
                      no_question += 1
                    # In case of invalid input, the Error Message will appear
                    else:
                      raise ValueError(cs("Invalid Answer", "red"))
                  except ValueError as a:
                    print(a) 
                  quiz_progressbar(no_question,num_questions)                
        # Same procedure as in "movies" loop
        elif choose == "literature":
          while no_question < num_questions:
              literature_dict = literature_allq[no_question]
              prompt = inquirer.prompt([
                       inquirer.List(
                              'choice',
                              message = literature_dict['message'],
                              choices = literature_dict['choices'],
                              ),
              ])
              answer = prompt['choice']
              if answer == literature_allq[no_question]["correct_choice"]:
                  count += 1
                  no_question += 1
                  quiz_progressbar(no_question,num_questions)
                  print(cs(f"\nGood job!You have {count} correct answer(s) out of {no_question}.\n", "green"))
              elif answer != literature_allq[no_question]['correct_choice']:
                  quiz_progressbar(no_question,num_questions)
                  print(cs(f"\nWrong, you have {count} correct answer(s) out of {no_question}.\n", "red"))
                  try:
                    help = yes_no("\nWould you like a hint and try again? (yes/no): ","pink")
                    if help == "yes":
                      print(cs(literature_allq[no_question]['hint'],"yellow"))
                    elif help == "no":
                      no_question += 1
                    else:
                      raise ValueError(cs("Invalid Answer", "red"))
                  except ValueError as a:
                    print(a)
                  quiz_progressbar(no_question,num_questions) 
        # Same procedure as in "movies" loop
        elif choose == "art":
          while no_question < num_questions:
              art_dict = art_allq[no_question]
              prompt = inquirer.prompt([
                       inquirer.List(
                              'choice',
                              message = art_dict['message'],
                              choices = art_dict['choices'],
                              ),
              ])
              answer = prompt['choice']
              if answer == art_allq[no_question]["correct_choice"]:
                  count += 1
                  no_question += 1
                  quiz_progressbar(no_question,num_questions)
                  print(cs(f"\nGood job!You have {count} correct answer(s) out of {no_question}.\n", "green"))
              elif answer != art_allq[no_question]['correct_choice']:
                  quiz_progressbar(no_question,num_questions)
                  print(cs(f"\nWrong, you have {count} correct answer(s) out of {no_question}.\n", "red")) 
                  try:
                    help = yes_no("\nWould you like a hint and try again? (yes/no): ","pink")
                    if help == "yes":
                      print(cs(art_allq[no_question]['hint'], "yellow"))
                    elif help == "no":
                      no_question += 1
                    else:
                      raise ValueError(cs("Invalid Answer", "red"))
                  except ValueError as a:
                    print(a)
                  quiz_progressbar(no_question,num_questions) 
        # The loop will break if user chooses to input "exit"
        elif choose == "exit":
          print(goodbye)
          break
        # When the inner loop is finished, the current question number and score count reset
        no_question = 0
        count = 0
    # If user enters anything else than the options liste, Error message will display
    except ValueError as e:
      print(e)
       
    
    
    
  

              

        
        
        
        
        
        
        


