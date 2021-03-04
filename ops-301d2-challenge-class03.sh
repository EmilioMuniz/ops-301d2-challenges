#!/bin/bash

# Script:                   ops-301d2-challenge-class03                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/03/2021    
# Purpose:                  Change permissions using chmod.

# Declaration of variables:


# Main:
echo Please enter directory path:

# Input: /opsfile.txt

read path

echo Heading to: $path

cd $path

echo Please enter permissions number:

read code

cd $path

ls -al

chmod -R 777 ./

ls -al

#End
