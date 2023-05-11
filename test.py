import csv #importing files with quiz questions
from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingSquaresBar #to show how much progress user made through the quiz
import function #stored all functions in a different file (module)
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
num_questions = len(questions) - 1
movies.close()


bar = FillingSquaresBar('Processing', max=num_questions)
count = 0
valid_options = ["a","b","c","d","A","B","C","D"]


#  Outputs a welcome message and lets the user decide the topic
print(cs("\nHello! Welcome to the Multiple Choice Quiz!","blue"))

while True:
    choose = input("\nChoose from the topics available by typing movies, literature or art or anything else to exit:\n").lower()
    if choose == "movies":
        for i, question in enumerate(questions):
            prompt = inquirer.prompt([
                inquirer.List('choice',
                              message=question['message'],
                              choices=question['choices'],
                              ),
            ])
            answer = prompt['choice']
            if answer == questions[i]["correct_choice"]:
              count += 1
              print(f"Good job!You have {count} correct answer(s).\n")
            elif answer != questions[i]['correct_choice']:
              print(f"Wrong, the right answer is {questions[i]['correct_choice']}")

              

        
        
        
        
        
        
        
        
                  # function.qalist_movies(i,questions)
                  # answer = input("Answer (A to D), or a 'hint': ").upper()
                  # if answer == "HINT":
                  #     print("\n", {questions[i][6]})
                  # elif answer == questions[i][5]:
                  #     count += 1
                  #     print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
                  #     if i < num_questions:
                  #       bar.next(1)
                  # elif answer != questions[i][5] and answer != "HINT":
                  #     print(cs(f"\n Wrong,the correct answer is {questions[i][5]}. You have {count} correct answer(s)\n", "red"))
                  #     if i < num_questions:
                  #       bar.next(1)
                  # elif answer not in valid_options:
                  #     print(cs("Please provide a valid answer","yellow"))
                  #     break

