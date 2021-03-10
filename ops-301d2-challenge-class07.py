#!/usr/bin/env python3

# Script:                   ops-301d2-challenge-class07.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/09/2021    
# Purpose:                  Using os.walk().

# Declaration of variables:
pathway = input("Please enter file path:")

# Declaration of functions:

# Main
import os

print(pathway)

for root, dirs, files in os.walk(pathway, topdown=True):
    print(root)
    print(dirs)
    print(files)

# End
# References: https://www.tutorialspoint.com/python/os_walk.htm
