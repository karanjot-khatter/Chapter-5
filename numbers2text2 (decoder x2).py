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
#This version using a list accumulator
def main():
    print("the program converts a sequence of unicode numbers into")
    print("the string of text that ist represents. \n")

    #get message to encode
    inString = input("Please enter the unicode-encoded message:")

    #loop through each substring and build unicode message
    chars = []
    for numStr in inString.split():
        codeNum = eval(numStr)  #converts digits to a number
        chars.append(chr(codeNum))  #accumulate new character - collect by appending them. Joining characters to ether using an empty string
    message = "".join(chars)
    print("\nThe decoded message is: ", message)
main()