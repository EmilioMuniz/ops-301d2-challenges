#!/usr/bin/env python3

# Script:                   ops-301d2-challenge-class13.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/17/2021    
# Purpose:                  Using "requests" library in python.

# Declaration of variables:


# Declaration of functions:

# Main
import requests
webpage = input("Enter destination URL:\n")
print("You are about to access URL:", webpage)
import inquirer
questions = [
  inquirer.List('method',
                message="Select HTTP method",
                choices=["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"],
            ),
]
answers = inquirer.prompt(questions)
print ("You are about requests HTTP:", answers['method'])
choice = input("Would you like to proceed? y/n""\n")
if choice == "y":
    g = requests.get(webpage)
    print(g.text)
elif choice == "n":
    print("Goodbye!")
