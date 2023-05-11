import csv #importing files with quiz questions
from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingSquaresBar #to show how much progress user made through the quiz
import function #stored all functions in a different file (module)

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
num_questions = len(questions) - 1
literature.close()

art = open("art_questions.csv", "r")
datareader = csv.reader(art)
art_q = []
for row in datareader:
  art_q.append(row)
num_questions = len(questions) - 1
art.close()

bar = FillingSquaresBar('Processing', max=num_questions)
i = 1 
count = 0
valid_options = ["a","b","c","d","A","B","C","D"]


#  Outputs a welcome message and lets the user decide the topic
print(cs("\nHello! Welcome to the Multiple Choice Quiz!","blue"))

while True:
  choose = input(cs("\nChoose from the topics available by typing movies,literature or art or anything else to exit: \n","purple")).lower()
  while choose == "movies" or choose == "literature" or choose == "art":
    if choose == "movies":
      for i in range(1,10):
            function.qalist_movies(i,questions)
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == "HINT":
                print(questions[i][6])
                function.hint(i)
                break
            elif answer == questions[i][5]:
                count += 1
                print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
                if i < num_questions:
                  bar.next(1)
            elif answer != questions[i][5] and answer != "HINT":
                print(cs(f"\n Wrong,the correct answer is {questions[i][5]}. You have {count} correct answer(s)\n", "red"))
                if i < num_questions:
                  bar.next(1)
            elif answer not in valid_options:
                print(cs("Please provide a valid answer","yellow"))
                break
    elif choose == "literature":
        while i <= num_questions:
            function.qalist_literature(i, literature_q)
            answer = input("Answer (A to D), or a 'hint': ").lower()
            if answer == "hint":
              print(literature_q[i][6])
              function.hint(i)
            elif answer == literature_q[i][5]:
              count += 1
              i += 1
              print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
              if i <num_questions:
                bar.next(1)
            elif answer != literature_q[i][5]:
              print(cs(f"\n Wrong,the correct answer is {literature_q[i][5]}. You have {count} correct answer(s)\n", "red"))
              if i <= num_questions:
                bar.next(1)
            else:
              print(cs("Please provide a valid answer","yellow"))
              break
    elif choose == "art":
        for i in range(1,10):
            function.qalist_art(i,art_q)
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == "hint":
              print(literature_q[i][6])
              function.hint(i)
            elif answer == art_q[i][5]:
              count += 1
              print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
              if i <num_questions:
                bar.next(1)
            elif answer in valid_options:
              print(cs(f"\n Wrong,the correct answer is {art_q[i][5]}. You have {count} correct answer(s)\n", "red"))
              if i < num_questions:
                bar.next(1)
            else:
              print(cs("Please provide a valid answer","yellow"))
              break
  else:
    print(cs("\nPlease provide a valid answer\n","yellow"))
    break

