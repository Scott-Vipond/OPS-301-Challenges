#!/bin/bash

# Script:                    Ops Challenge 04
# Author:                    Scott Vipond   
# Date of latest revision:   15 Dec 22   
# Purpose:                   Conditionals in Menu System

# Tasks:
    # Create a bash script that launches a menu system with the following options:
        # Hello world (prints “Hello world!” to the screen)
        # Ping self (pings this computer’s loopback address)
        # IP info (print the network adapter information for this computer)
        # Exit
    # Next, the user input should be requested.
    # The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
    # Use a loop to bring up the menu again after the request has been executed.


# Reference sites below:
# https://linuxhint.com/bash_conditional_statement/
# https://www.geeksforgeeks.org/bash-scripting-else-if-statement/
# https://askubuntu.com/questions/200989/ping-for-4-times

menu=5

while [ $menu != 4 ]
do
    echo "Menu Items Available:"
    echo "1. Print Hello World!"
    echo "2. Ping computer loop back"
    echo "3. Print computer IP info"
    echo "4. Exit"

    echo "What option would you like to perform, please enter number (i.e. 1, 2, etc.)? "
    read menu

        if (( $menu == 1 ))
        then 
            echo # creates some space in menu iterations
            echo # creates some space in menu iterations
            echo "Hello World!"
            echo # creates some space in menu iterations
            echo # creates some space in menu iterations
        elif (( $menu == 2 ))
        then 
            echo # creates some space in menu iterations
            echo # creates some space in menu iterations
            ping -c 4 127.0.0.1
            echo # creates some space in menu iterations
            echo # creates some space in menu iterations
       elif (( $menu == 3 ))
       then 
            echo # creates some space in menu iterations
            echo # creates some space in menu iterations
            ip a
            echo # creates some space in menu iterations
            echo # creates some space in menu iterations
       else (( $menu == 4))
            echo # creates some space in menu iterations
            echo # creates some space in menu iterations
            echo "Thank you for using my script"
        fi
done

# End