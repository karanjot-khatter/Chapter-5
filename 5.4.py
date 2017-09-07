#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     30/08/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("When you enter a phrase, it will output the acronym all in uppercase")
    phrases = input("Please enter a phrase:")
    acronym = "".join(phrases[0] #concatonate first letters of string
    for phrases in phrases.upper().split()) #allows to be in a list
    print("The acronym for:", phrases, "is:", acronym)
main()