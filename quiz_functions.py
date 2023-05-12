from stringcolor import cs #importing one module from stringcolor, to change the color of text
from progress.bar import FillingCirclesBar #to show how much progress user made through the quiz
def user_input(topics,color):
  choose = input(cs(topics,color)).lower()
  return choose

  



  