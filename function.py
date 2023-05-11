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
def hint(i):
    if i > 1:
      i = i - 1
      return i 
    elif i <= 1:
      i = 1 
      return i