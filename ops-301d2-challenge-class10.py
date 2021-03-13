#!/usr/bin/env python3

# Script:                   ops-301d2-challenge-class10.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/12/2021    
# Purpose:                  Using conditional statements in python.

# Declaration of variables:
a = int(100)
b = int(100)

# Declaration of functions:

# Main
if a < b:
    print("a is less than b.")
elif b > a:
    print("b is greater than a.")
elif a != b:
    print("a is not equal to be.")
elif a == b:
    print("a is equal to b.")

if a != b:
    print("a is not equal to b.")
elif a > b:
    print("a is greater than b.")
else:
    print("a is equal to b.")

# End
# References: https://github.com/codefellows/seattle-ops-301d2/blob/main/class-10/challenges/DEMO.md
