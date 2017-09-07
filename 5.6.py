#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     31/08/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This prgoram calculates the numerical value fo a full name provided as input")
    nameInput = input("Please enter a full name:").lower()
    sum = 0
    for ch in nameInput.replace(" ",""): #this eliminates the blanks
        sum +=ord(ch) -96
    print(sum)

main()
