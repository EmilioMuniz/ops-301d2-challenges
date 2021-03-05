#!/bin/bash

# Script:                   ops-301d2-challenge-class04                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/04/2021    
# Purpose:                  Use Bash conditional statement to launch menu.


# Main:
until [[ $n = 0 ]];do
echo -n "Menu Options: 
                       1) Hello World!
                       2) Ping
                       3) IP Info
                       0) Exit
                       Enter a number:"
read n 
if (($n == 1)); then
echo "Hello World!"
elif (($n == 2 )); then
ping -c 4 127.0.0.1
elif (($n == 3)); then
ip a
elif (($n == 0)); then
exit  
fi                       
done                        
# End
# References: https://linuxhint.com/bash_conditional_statement/ https://techstop.github.io/menu-bash-script/
