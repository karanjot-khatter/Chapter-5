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

#This program adds files in the string together and display in another file
def addUpPairs2():
    inName= input("Enter the input file:")
    outName = input("Enter the output file: ")
    inFile = open(inName,"r")
    outFile = open(outName, "w")
    for line in inFile:
        pairOfStrings = line.split()
        number1 = eval(pairOfStrings[0])
        number2 = eval(pairOfStrings[1])
        print(number1 + number2, file = outFile)
    inFile.close()
    outFile.close()

addUpPairs2()
