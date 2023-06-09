### Link to my repository: https://github.com/Mira-cs/terminal_application  
### Link to my presentation: https://youtu.be/oQV4mxSbq2Q 
---------------------------------------------------------------- 
## References (resources that helped me with the assignment)  
A gentle introduction to testing with pytest (no date) A Gentle Introduction to Testing with PyTest - Bas codes. Available at: https://bas.codes/posts/python-pytest-introduction  
Hira, Z. (2023) Bash scripting tutorial – linux shell script and command line for Beginners, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/  
Working with CSV files in Python (2023) GeeksforGeeks. Available at: https://www.geeksforgeeks.org/working-csv-files-python/       
Python enhancement proposals (no date) PEP 8 – Style Guide for Python Code. Available at: https://peps.python.org/pep-0008/   
Shellcheck (no date) ShellCheck. Available at: https://www.shellcheck.net/  

----------------------------------------------------------------
## Style guide 

The style guide I followed: **PEP8** (for easier readability)   
- Used 4 spaces indentation level  
- Brackets,parenthesis lined up under the first character of the line that starts the multiline construct  
- Comments are block elements that start with the capital letter without periods  
- Spaces after each comma, but not before  
- Spaces around the variables
- Snake case used to declare variables
- Surrounding functions with two blank lines    

----------------------------------------------------------------
## A list of features of the terminal application (Quiz):
- **Being able to choose topic and one options out of four presented**  
I came up with three topics for the quiz as well as 9 questions for each topic as well as 4 possible answers. In the beginning users are able to choose one topic out of three.Then, according to the answer they provide, they will be asked 9 questions in an order of their index. 
- **Score count**   
The program counts the number of questions the user did right, providing the overall score out of total number of questions whenever the progress is made. 
- **Hints**  
User can also request a hint in case they are struggling.I created a separate hint file that is then imported into the python file, just like the quiz questions.So whenever user makes a wrong choice, the program will ask if they want a hint. If the hint isnt needed,the quiz will move on to the next question,if the user says "yes" to the hint, then the program will output a hint while going back to the previous question.
- **Progress Bar**   
User will be able to see what stage of the quiz they are at with the help of the Progress Bar.The percentage will be displayed in the progress bar, letting the user know how far along in the quiz they are.
----------------------------------------------------------------
## Implementation Plan  
#### Link to my Trello board:   
#### https://trello.com/b/aIu5ZHc6/terminal-application-ip  
### Pictures of my Trello Board:  
!['Trello board screenshot'](https://i.ibb.co/3N1WF9y/trello.png)  
!['Trello board screenshot'](https://i.ibb.co/TbdHNZN/trello1.png) 
!['Trello board screenshot'](https://i.ibb.co/yQBFwhB/trello2.png) 
!['Trello board screenshot'](https://i.ibb.co/JBRSFH5/trello3.png)

### Feature 1: May 5th - May 8th   
**Giving user an opportunity to choose a topic from three available:**  
The quiz will give the user an opportunity to choose a topic for the quiz. To do so, I had to come up with three topics and 9 questions for each.I used Excel to write down all the questions,options, hints and correct answers. Then I exported it into a CSV files.CSV files are then added to the same folder as the quiz.py file. Every file is opened and iterated over, creating lists and dictionaries inside them."valid_options" variable is declared. It contains a list of strings reprenseting the options users can choose from (topics) and in case of invalid input, an Error message will be displayed. This variable makes it possible to match the input to the valid options offered by the app. 

**Checklist:**
1) Creating three CSV files (movies,art,literature) with questions, options, correct answers and hints in them 
2) Importing CSV module into the main file  (quiz.py)
3) Opening the files and making the program iterate over them and create dictionary
4) Dictionaries are then passed in the list under corresponding variables with the append() function
5) The headers of each CSV file is skipped (because it's the headline of the columns), files are closed
6) Prompting user to input a topic they are intersted in taking the quiz in (input() function)
7) If input is not in "valid_options" variable, program will display an Error message (try/except statements)
8) Give user an opportunity to exit the program if they wish (if they type in "exit" message,program stops executing) 
9) Program will keeps asking to participate in the quiz unless the "exit" message is inputted 

### Feature 2: May 8th - May 10th   
**Score count**   
Everytime user makes correct choice their score increases. In case of incorrect choice program won't add it to the score. "count" variable was declared which starts out with the value of 0.Everytime the program iterates over the questions, "if" statement makes sure the choice made is the correct one, and if thats the case, it adds 1 to the count.The program will also display the score after every question.After the completion of the quiz, "count" resets to 0 again. 
**Checklist:**
1) Iterate over the questions using loops as long as there are questions available (len(questions))
2) Declare a "count" variable and assign value of 0 to it 
3) Make the program match the answer chosen with the correct answer with "if" statements (if answer == correct answer:)
4) Increase the score count if the answer is correct (if answer == correct answer: count += 1)
5) The count stays the same in case of the wrong choice (if answer != correct answer:)
6) Count resets in the end of the quiz. The end of inner loop: count = 0

### Feature 3: May 8th-May 12th  
**Hints**   
Users are able to use hints in case they need to (there is no limit).The program prompts user to choose if they would want to use a hint in case they are struggling (the program only offers a hint if user chooses the wrong option). Users are able to say "yes" or "no" to a hint.If "yes", hint and previous question will be displayed,if "no", user moves on to the next question.  
**Checklist:**
1) Create an input asking if the user would like to use a hint and try again
2) Create "if" statements (in case of yes, no and invalid inputs)
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
4) Use appropriate function to make bar go up by 10% everytime the question is answered with 2 arguments, number of current question and total number of questions
5) Make sure the progress bar is implemented after right/wrong answers correctly
 
----------------------------------------------------------------
## Help Documentation  
This section of the file contains instructions on how to install and operate the Multiple Choice Quiz terminal application.

### Requirements

Python 3.0 or higher is required  
Git

### Installation Steps:

1) Clone my GitHub repository from the following link:  
https://github.com/Mira-cs/terminal_application
2) Open terminal window
3) Use "cd" command to go to the root folder of the repository you downloaded
4) Make sure you are running the following commands in virtual environment (to do so, run "source venv/bin/activate" command)
5) Run the "chmod +x wrapper.sh" command in terminal 
6) Execute "./wrapper.sh" file
7) Follow the steps provided in the script 
8) Bash will run quiz.py file 

### List of Dependencies  

blessed==1.20.0  
colorama==0.4.6  
Columnar==1.4.1  
iniconfig==2.0.0  
inquirer==3.1.3  
packaging==23.1  
pluggy==1.0.0  
progress==1.6  
prompt-toolkit==3.0.38  
pyfiglet==0.8.post1  
pytest==7.3.1  
python-editor==1.0.4  
readchar==4.0.5  
six==1.16.0  
string-color==1.2.3  
toolz==0.12.0  
wcwidth==0.2.6  

### System/Hardware Requirements 
- OS system that supports Python 3.0  or higher, that includes Windows, MacOs, Linux distributions
- 70 MB of free disk space 
- 512 MB of RAM








