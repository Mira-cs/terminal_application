### Link to my repository: https://github.com/Mira-cs/terminal_application  
## References (resources that helped me with the assignment)   

## Style guide 

The style guide I followed: **PEP8** (for easier readability)   
- Used 4 spaces indentation level  
- Brackets,parenthesis lined up under the first character of the line that starts the multiline construct  
- Comments are block elements that start with the capital letter without periods  
- Spaces after each comma, but not before  
- Spaces around the variables
- Snake case used to declare variables
- Surrounding functions with two blank lines    

### Reference:   
Python enhancement proposals (no date) PEP 8 – Style Guide for Python Code. Available at: https://peps.python.org/pep-0008/ 

----------------------------------------------------------------
## A list of features of the terminal application (Quiz):
- **Being able to choose topic and one options out of four presented**  
I came up with three topics for the quiz as well as 9 questions for each topic as well as 4 possible answers. In the beginning users are able to choose one topic out of three.Then, according to the answer they provide, they will be asked 9 questions in a certain order. 
- **Score count**   
The program counts the number of questions the user did right, providing the overall score after every question.
- **Hints**  
User can also request a hint in case they are struggling.I created a separate hint file that is then imported into the python file, just like the quiz questions.So whenever user makes a wrong choice, the program will ask if they want a hint. If the hint isnt needed,the quiz will move on to the next question,if the user says "yes" to the hint, then the program will output a hint while going back to the previous question.
- **Progress Bar**   
User will be able to see what stage of the quiz they are at with the help of the Progress Bar.The percentage will be displayed in the progress bar, letting the user know how far along they are.
## Implementation Plan  
#### Link to my Trello board:   
#### https://trello.com/b/aIu5ZHc6/terminal-application-ip
-----------------------------------------------------------------
### Feature 1: May 5th - May 8th   
**Giving user an opportunity to choose a topic from three available:**
As I explained earlier, the quiz will give the user an opportunity to choose a topic for the quiz. To do so, I had to come up with three topics and questions for each.I used Excel to write down all the questions,options, hints and correct answers. Then I exported it into a CSV files.CSV files are then added to the same folder as the quiz.py file. Every file is opened and iterated over, creating lists and dictionaries inside them."Valid_options" variable is created. It contains strings reprenseting the options users can choose from (topics) and in case of invalid input, an Error message will be displayed.

**Checklist:**
1) Creating three CSV files (movies,art,literature) with questions, options, correct answers and hints in them 
2) Importing these files into the main file  (quiz.py)
3) Opening the files and making the program iterate over them and create dictionary 
4) Dictionaries are then passed in the list under corresponding variables with the append() function
5) Prompting user to input a topic they are intersted in taking the quiz in (input() function)
6) If input is not in "valid_options" variable, program will display an Error message (try/except statements)
7) Give user an opportunity to exit the program if they wish (if they type in "exit" message,program stops executing) 
8) Program will keeps asking to participate in the quiz unless the exit message is inputted 

### Feature 2: May 8th - May 10th   
**Score count**   
Everytime user makes correct choice their score increases. In case of incorrect choice program won't add it to the score. I created a count variable that starts out with the value of 0.Everytime the program iterates over the questions, if statement makes sure the choice made is the correct one, and if thats the case, it adds 1 to the count.The program will also display the score after every question.After the completion of the quiz, score resets to 0 again.It was made possible because the program matches correct answers to the one user chose.  
**Checklist:**
1) Iterate over the questions using loops as long as there are questions available (len(questions))
2) Create a variable and assign value of 0 to it, 
3) Make the program match the answer chosen with the correct answer with if statements (if answer = correct answer)
4) Increase the score count if the answer is correct (if answer = correct answer: count += 1)
5) The count stays the same in case of the wrong choice 
6) Count resets in the end of the quiz 

### Feature 3: May 8th-May 12th  
**Hints**   
Users are able to use hints in case they need to (there is no limit).The program prompts user to choose if they would want to use a hint in case they are struggling (the program only offers a hint if user chooses the wrong option). Of course, users are able to say yes or no to a hint.If yes, hint and previous question will be displayed,if no, user moves on to the next question.  
**Checklist:**
1) Create an input asking if the user would like to use a hint and try again
2) Create if statements (in case of yes, no and invalid inputs)
3) Implement a try/except statement for invalid inputs, displaying an error message
4) Make the program match hint to the current question and print it out (if yes)
5) If no, make program move on to the next question by adding 1 to the number of current question  
  
### Feature 4: May 8th-May 12th  
**Progress Bar**  
Users are able to see how far along they are in the quiz with the help of the Progress Bar (the package progressbar was imported from Pypi).The progress bar goes up by 10% every time the question is answered.  
**Checklist:** 
1) Install a package from Pypi
2) Import progressbar package into the main file (not the entire package, but certain modules)
3) Create a variable for the bar of a certain class and pass arguments to the function (message,length)
4) Use appropriate function to make bar go up by 10% everytime the question is answered
5) Reset the bar after the quiz is completed







