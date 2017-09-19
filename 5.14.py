#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     09/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program should print the number of lines, words and characters in a file")
    fileName = input("Enter the file name:") #don't forget the .txt
    inFile = open(fileName, "r")
    words = 0
    lines = 0
    chars = 0
    for line in inFile:
        lines = lines + 1
        chars = chars +len(line) #len returns the length of object. for each object
        words = words + len(line.split()) #length of line split.

    print("Number of lines:", lines)
    print("Number of words in file:",words)
    print("Number of characters:", chars)
main()