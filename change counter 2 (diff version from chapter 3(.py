#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     22/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#program calculates the value of some change in dollas
#This verrsion represnets the total cash in cents
def main():

    print("Change counter\n")
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters:"))
    dimes = eval(input("Dimes:"))
    nickels = eval(input("Nickels:"))
    pennies = eval(input("Pennies:"))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("The total value of your change is ${0}.{1:0>2}".format(total//100, total % 100))
    #0 - put as much space as you need
    #precission 2, round to 2 d.p

main()