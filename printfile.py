#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     23/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Prints a file to the screen e.g. pairs.py
def main():
    fname = input("Enter filename:")
    inFile = open(fname,"r")
    data = inFile.read()
    print(data)
main()