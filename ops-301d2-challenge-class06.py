#!/usr/bin/env python3

# Script:                   ops-301d2-challenge-class06.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/08/2021    
# Purpose:                  Using Bash commands in Python.

# Declaration of variables:
var1 = "whoami"
var2 = "ip a"
var3 = "lshw -short"

# Declaration of functions:

# Import Libraries
import os

print("Username:")

os.system(var1)

print("IP Information:")

os.system(var2)

print("Hardware Informatin:")

os.system(var3)



# End
# References: https://docs.python.org/3/library/os.html https://www.python.org/dev/peps/pep-0008/
