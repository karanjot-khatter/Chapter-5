#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Karanjot
#
# Created:     07/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
#2000 principal, 0.1 apr, 7 years - same as textbook

    principal = eval(input("Enter the intial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))
    print("{0}".format("Year"), "{0:12}".format("Value"))
    print("-------------")
    print("{0:4}".format(0), "{0:1.2f}".format( principal))
    for i in range(years):
        principal = principal * (1 + apr)
        print("{0:4}".format(i+1), "{0:1.2f}".format( principal))

main()
