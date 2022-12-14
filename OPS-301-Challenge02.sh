#!/bin/bash

# Script:                    Ops-301 Challenge 02
# Author:                    Scott Vipond   
# Date of latest revision:   13 Dec 22   
# Purpose:                   Append text file; use Date and Time  


# Tasks:
  # copy the /varlog/syslog file to the current directory
    
  # append the syslog with the current date and time

# Reference sites below:
# https://www.cyberciti.biz/faq/unix-linux-getting-current-date-in-bash-ksh-shell-script/
# https://replit.com/@HexxKing1/Ops-301d7-Challenge-02#main.sh

# Variables for the different portions of the date and time needed for script, none were used in script
# year=`date +%Y`
# month=`date +%m`
# day=`date +%d`
# hour=`date +%H`
# minute=`date +%M`
# second=`date +%S`

# Test echo commands to ensure above variables function as expected
# echo `date`
# echo "Current Date: $day-$month-$year"
# echo "Current Time: $hour:$minute:$second"

# Copies the syslog to the current directory
cp /var/log/syslog .

# Appends the above syslog in current directory with the current date and time
'date' >> syslog

# End