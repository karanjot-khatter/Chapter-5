#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     14/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#username
#string processing program to generate username

def main():
    print("This program generates computer usernames. \n") #\n puts an extra line
    #get users first and last name
    first = input("Please enter your first name (all lowercase) : ")
    last = input("Please enter your last name (all lowercase) :")

    #concatenate first intiial with 7 char of the last name
    usname = first[0] + last [:7]

    #output username
    print("Your username is: ", usname)
main()