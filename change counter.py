#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     13/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("Change  counter")
    #manipulates 5 different types of values - float / int
    quarters = eval(input("Please enter the amount of quarters?"))
    dimes = eval(input("Please enter the amount of dimes?"))
    nickels = eval(input("Please enter the amount of nickels?"))
    pennies = eval(input("Please enter the amount of pennies?"))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01) #fractional numbers / float
    print("The total amount is:", total)

main()