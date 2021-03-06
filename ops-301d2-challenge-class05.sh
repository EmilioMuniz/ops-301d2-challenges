#!/bin/bash

# Script:                   ops-301d2-challenge-class05                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/04/2021    
# Purpose:                  Script to clear logs.

# Declaration of variables:

# Declaration of functions:

# Run as root user.

# Main:
cat /var/log/syslog

cat /dev/null > /var/log/syslog

cat /var/log/syslog

cat /var/log/wtmp

cat /dev/null > /var/log/wtmp

cat /var/log/wtmp

echo "All Done."

# End

# Resources: https://www.tecmint.com/empty-delete-file-content-linux/
