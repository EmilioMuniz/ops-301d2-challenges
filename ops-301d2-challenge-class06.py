#!/usr/bin/env python3

# Script:                   ops-301d2-challenge-class06.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/08/2021    
# Purpose:                  Using Bash commands in Python.

# Declaration of variables:
var1="This is your username:"
var2="This is your ip info:"
var3="This is your system info:"

# Declaration of functions:

# Import Libraries
import os

print(var1)

os.system("whoami")

print(var2)

os.system("ip a")

print(var3)

os.system("lshw -short")



# End
# References: https://docs.python.org/3/library/os.html https://www.python.org/dev/peps/pep-0008/
