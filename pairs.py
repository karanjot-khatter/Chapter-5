#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     14/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#This program adds files in the string together and display on the screen
def addUpPairs():
    fileName = input("Enter the file name:") #don't forget the .txt
    inFile = open(fileName, "r")
    for line in inFile:
        pairsOfStrings = line.split() #convert each line of the file into a list of 2 strings
        number1 = eval(pairsOfStrings[0]) #converted into numbers by eval before being added
        number2 = eval(pairsOfStrings[1])

        print(number1 + number2)
    inFile.close()

addUpPairs()