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
            codedMessage += chr((ord(ch) - 97 + inputValue) % 26 + 97)#encode hence plus ASCII from 97 - 122. therefore letter range 0 -25 (26 letters). a = 97
    elif inputEorD =="d":
        for ch in inputText:
            codedMessage += chr((ord(ch) - 97 - inputValue) % 26 + 97)#decode hence minus
    else:
        print("You did not enter E/D! Try again!!")
    print("The text inputed:", inputText,  ".Is:", inputEorD, ".By the key of",inputValue, ".To make the message", codedMessage)

main()

