#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     22/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#A program to convert a sequence of unicode numbers into
#a string of text

def main():
    print("This program converts a sequence of unicode numbers into ")
    print("the string of text that it represent.\n ")

    inString = input("Please enter the Unicode-encoded message:")

    #loop thorugh each substring and build unicode message
    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr) # convert digit to number
        message = message + chr(codeNum) #concatenate character to message - create a complete copy of the message so far
    print("\nThe decoded message is:", message)
main()