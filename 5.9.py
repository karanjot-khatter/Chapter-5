#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     07/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program counts the number of words in a setence entered by the user")
    sentence = input("Please type in a sentence")
    word = 1
    char = 0
    for i in sentence:
        char=char+1
        if (i == " "):
            word = word + 1
    print("Number of words in the string:")
    print(word)
    print("Number of characters in the string:")
    print(char)

main()