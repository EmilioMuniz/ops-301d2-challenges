#!/usr/bin/env python3

# Script:                   ops-301d2-challenge-class11.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/15/2021    
# Purpose:                  Using file handling commands in python.

# Declaration of variables:


# Declaration of functions:

# Main
f = open("class11file.txt", "a")
f.write("This is line 1.")
f.write("\n")
f.write("This is line 2.")
f.write("\n")
f.write("This in line 3.")
f = open("class11file.txt", "r")
print(f.readline())
import os
if os.path.exists("class11file.txt"):
  os.remove("class11file.txt")
# End
# References: https://w3schools.com/python/, https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
