#!/bin/bash

# Script:                   ops-301d2-challenge-class02                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  3/02/2021    
# Purpose:                  Append Date Time to Syslog File and copy to working directory.

# Declaration of variables:
year=`date +%Y`
month=`date +%m`
day=`date +%d`
hour=`date +%H`
minute=`date +%M`
second=`date +%S`

# Main:
touch "syslogcopy.txt_$(date +"%F %T")"

cd /var/log

sudo cp syslog ~/github/ops-301d2-challenges/"syslogcopy.txt_$(date +"%F %T")"

echo All Done

#End

# Resources: https://stackoverflow.com/questions/48270960/how-to-create-a-file-with-todays-date-in-the-filename https://stackoverflow.com/questions/22589984/copying-syslog-file-to-a-new-directory-in-linux
