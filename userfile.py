#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Karanjot
#
# Created:     05/06/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Program to create a file of usernames in batch mode
#batch names in names.txt
#second file - creates new file

def main():
    print("This program creates a file of usernames from a file of names")

    #get the file names
    inFileName = input("What file are the names in?")
    outFileName = input("What file should the usernames go in?")

    #open the files
    inFile = open(inFileName, "r")
    outFile = open(outFileName, "w")

    #process each line of the input file
    for line in inFile:
        #get the first and last name from line
        first, last = line.split()
        #create the username
        uname = (first[0] + last[:7]).lower()
        #write it to the output file
        print(uname, file = outFile)

    inFile.close()
    outFile.close()
    print("Usernames have been written to", outFileName)

main()