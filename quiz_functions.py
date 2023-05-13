from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingCirclesBar #to show how much progress user made through the quiz

#function used in the app to take users input(choosing a topic)
def user_input(topics,color):
  choose = input(cs(topics,color)).lower()
  return choose
 
 
def yes_no(topics,color):
  help = input(cs(topics,color)).lower()
  return help
 

#function used for testing purposes
def is_valid_input(message,color):
  # Storing the user input in the variable "text"
  text = input(cs(message,color)).lower()
  # Storing list of items in the variable "valid_options"
  valid_options = ["movies", "literature", "art", "exit"]
  # Iterating through the list and storing each item in the option variable
  for option in valid_options:
    # If the input is equal to the item stored in option variable, return True, else, return False
    if text == option:
      return True
  return False


# Function made for the progress bar
def quiz_progressbar(question_no,numb_questions):
  # Passing two instance into the class FillinCirclesBar, text "Progress" and length  
  bar = FillingCirclesBar("Progress",max = numb_questions)
  # If statement, which makes bar progress if the current question number is less than the total
  if question_no <=  numb_questions:
    # Bar will progress by the number of the current question
    bar.next(question_no)



  



  