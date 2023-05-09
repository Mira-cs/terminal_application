### Link to my repository: https://github.com/Mira-cs/terminal_application
### A list of features of the terminal application (Quiz):
- **Being able to choose topic and one options out of four presented**  
I came up with three topics for the quiz as well as 9 questions for each topic as well as 4 possible answers. In the beginning users are able to choose one topic out of three.Then, according to the answer they provide, they will be asked 9 questions in a certain order. I stored questions and options in the CSV file,which is then imported into the python program.  
The quiz itself is executed with the help of "while" and "for" loops
"While" will keep looping as long as the answers provided are valid. "For" loop will execute as long as there are questions available.
- **Score count**   
The program counts the number of questions the user did right, providing the overall score in the end.In case of incorrect input, the program will output the correct answer as well as the score.
- **Hints**  
User can also request a hint in case they are struggling.I created a separate hint file that is then imported into the python file, just like the quiz questions.



