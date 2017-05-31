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

def main():
    #months is a list used as a lookup table - instead of abbrievation
    months = ["January", "Febuary","March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
    n = eval(input("Please enter a number a number between 1-12:"))
    print("The month is", months[n-1] +".")
main()