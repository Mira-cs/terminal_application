## Outline of the testing procedures ##  
### Purpose: 
To test bits of code and confirm that they are executed correctly, the way they were intended to, for the app to perform smoothly.  
### Plan: 
Pytest was imported and used for the testing purposes. Since the testing is done to check the functionality of the code, it would fall under unit testing area.  
Two features were tested with pytest:   
**1. Taking user input and matching it to the correct topic**  
Since the variable valid_options was created with strings of the words that are then matched and used to direct user to the right topic (loop), it is important to make sure that the program executes it according to what the input was. Testing is only done to see what happens in different scenarios (valid/invalid input).
**2. Progress Bar**
Since progress bar has to show user's progress after every question, it's crucial for the bar to display an increase of the percentage without a fail. So, pytest will be checking if the progress bar starts out with the value of 0 and increases each time when the .next() is called.
### Test Cases  
**Feature 1:**
- Case 1: Enter a string "movie" as the input and check if the result is True, meaning it matches the options available
- Case 2: Enter a string of random numbers as the input  and check if the result is False, meaning it doesn't match the options available   
Each test case is tested in the same fashion as the above two. 
**Feature 2:**
- Case 1: Checking if the bar starts out at the value of 0
- Case 2: Asserting that the value goes up by one after calling the next()
- Case 3: Asserting that the value of the bar is equal to the number of quiz questions after iterating through "for" loop   

### Conclusion 
After testing each feature with pytest, it was confirmed that the code works as expected. 





