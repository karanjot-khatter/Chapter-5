#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     05/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def encrypt (cleartext):
    key = eval(input("Please enter the shift key: "))
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cyphertext = ""
    for char in cleartext:
        if char in alpha:
            newpos = (alpha.find(char) + key) % 26  #minus for decryption
            cyphertext += alpha[newpos]
        else:
            cyphertext += char
    return cyphertext

cleartext = input("Cleartext:").lower()
print(encrypt(cleartext))

