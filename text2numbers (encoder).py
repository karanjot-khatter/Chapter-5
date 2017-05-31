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
#program to convert a textual message ubti a sequence of
#numbers, utilizing the underlying unicode encoding

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the unicode encoding of the message")

#Got the message to encode
    message = input("Please enter the message to encode: ")
    print("\nHere are the UniCode codes: ")

    #loop through the message and print out the unicode values
    for ch in message:
        print(ord(ch),end=" ")
    print() #blank line before prompt
main()