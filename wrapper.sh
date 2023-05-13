#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
      read -p "Do you have all dependencies installed?(y/n): " answer
      if [[ $answer == [Yy] ]];
        then
          echo "Great,running the file..."
          python3 testing.py
       else
         read -p "Would you like all dependencies installed?(y/n): " answer
          if [[ $answer == [Yy] ]];
            then
              pip3 install string-color
              pip3 install inquirer
              pip3 install progress
              pip3 install pyfiglet
              python3 quiz.py
          else
            echo "Please install all dependencies first"
          fi
      fi
    else
        echo "Please install the Python later version on this website https://www.python.org/downloads/ " >&2
    fi 
else
    echo "You can install Python here https://www.python.org/downloads/" >&2
fi
