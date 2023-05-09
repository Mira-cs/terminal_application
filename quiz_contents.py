import csv #importing files with quiz questions
from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingSquaresBar #to show how much progress user made through the quiz

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
#  Outputs a welcome message and lets the user decide the topic
print(cs("\nHello! Welcome to the Multiple Choice Quiz!","blue"))
count = 0
valid_options = ["a","b","c","d","A","B","C","D"]
while True:
  choose = input(cs("\nChoose from the topics available by typing movies,literature or art or anything else to exit: \n","purple")).lower()
  if choose == "movies" or choose == "literature" or choose == "art":
    if choose == "movies":
      for i in range(1,10):
            print("\nQuestion ",i , "-", questions[i][0])
            print("A", questions[i][1])
            print("B ", questions[i][2])
            print("C ", questions[i][3])
            print("D ", questions[i][4])
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == questions[i][5]:
              count += 1
              print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
              if i < num_questions:
                bar.next(1)
            elif answer in valid_options:
              print(cs(f"\n Wrong,the correct answer is {questions[i][5]}. You have {count} correct answer(s)\n", "red"))
              if i < num_questions:
                bar.next(1)
            else:
              print(cs("Please provide a valid answer","yellow"))
    elif choose == "literature":
        for i in range(1,10):
            print("\nQuestion ", i , "-", literature_q[i][0])
            print("A", literature_q[i][1])
            print("B ", literature_q[i][2])
            print("C ", literature_q[i][3])
            print("D ", literature_q[i][4])
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == literature_q[i][5]:
              count += 1
              print(cs(f"\n Correct,you have {count} correct answer(s)\n","green"))
              if i <num_questions:
                bar.next(1)
            elif answer in valid_options:
              print(cs(f"\n Wrong,the correct answer is {literature_q[i][5]}. You have {count} correct answer(s)\n", "red"))
              if i < num_questions:
                bar.next(1)
            else:
              print(cs("Please provide a valid answer","yellow"))
              break
    elif choose == "art":
        for i in range(1,10):
            print("\nQuestion ", i , "-", art_q[i][0])
            print("A", art_q[i][1])
            print("B ", art_q[i][2])
            print("C ", art_q[i][3])
            print("D ", art_q[i][4])
            answer = input("Answer (A to D), or a 'hint': ").upper()
            if answer == art_q[i][5]:
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
    # if count >= 8:
    #   print(cs(f"\nWow,good job, you have {count} correct answer(s) out of {i} questions!\n", "purple"))
    #   yes_no = input("Would you like to take quiz again?: ")
    #   if yes_no == "yes":
    #     continue
    #   else:
    #     break
    # elif count <= 7:
    #   print(cs(f"\nYou have {count} correct answer(s) out of {i}.Don't worry, you can always play again!\n", "purple"))
    #   yes_no = input("Would you like to take quiz again?: ")
    #   if yes_no == "yes":
    #     continue
    #   else:
    #     break
  else:
    print(cs("\nPlease provide a valid answer\n","yellow"))
    break

