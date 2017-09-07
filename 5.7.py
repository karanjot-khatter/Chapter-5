#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     06/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program can encode and decode Caesar Ciphers") #e.g. if key value is 2 --> word shifted 2 up e.g. a would be c
    #input from user
    inputText = input("Please enter a string of plaintext:").lower()
    inputValue = eval(input("Please enter the value of the key:"))
    inputEorD = input("Please enter e (to encrypt) or d (to decrypt) ")
    #initate empty list
    codedMessage = ""
    #for character in the string
    if inputEorD == "e":
        for ch in inputText:
         x = chr(ord(ch) + inputValue) #formulae in book for encyrption
         if ch == ' ': #spaces
           codedMessage += ' '
        else: #no spaces then add into the string
            codedMessage += chr(ord(ch) + inputValue)
    elif inputEorD =="d":
        for ch in inputText:
         x = chr(ord(ch) - inputValue) #formulae in book for decryption
         if ch == ' ': #spaces
           codedMessage += ' '
        else: #no spaces then add into the string
            codedMessage += chr(ord(ch) - inputValue)

    else:
        print("You did not enter E/D! Try again!!")
    print("The text inputed:", inputText,  ".Is:", inputEorD, ".By the key of",inputValue, ".To make the message", codedMessage)

main()


