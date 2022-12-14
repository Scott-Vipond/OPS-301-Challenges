#!/bin/bash

# Script:                    Ops Challenge 03
# Author:                    Scott Vipond   
# Date of latest revision:   14 Dec 22   
# Purpose:                   Illustrate changing permissions on a directory and its contents 


# Tasks:
    # Prompts user for input directory path.
    # Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
    # Navigates to the directory input by the user and changes all files inside it to the input setting.
    # Prints to the screen the directory contents and the new permissions settings of everything in the directory.


# Reference sites below:
# https://github.com/codefellows/seattle-ops-301d7/blob/main/class-03/challenges/DEMO.md


# Ask user for directory path
echo "Please enter directory path: "
read dirpath

#Create directory for user path and change into it
mkdir $dirpath
sleep .5 #allows computer to create user directory
cd $dirpath #still unable to cd into user diretory after 45 minutes of testing

#Create a testfile to illustrate permission changes
touch testfile.txt

# Ask user what permission for the directory
echo "Please enter permissions number for directory (i.e. 777, 755, 764): "
read permnumber

# Change permissions for the entire directory
chmod --recursive $permnumber .

#  List permissions for the entire directory
ls -al .

# End