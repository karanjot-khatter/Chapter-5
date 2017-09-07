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
    print("This prgoram calculates the numerical value foa  single name provided as input")
    nameInput = input("Please enter a single name:").lower()
    sum = 0
    for ch in nameInput:
        sum +=ord(ch) -96
        #ord "a" returns value of 97. Hence why we take away 97
    print(sum)

main()