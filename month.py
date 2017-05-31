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
#month
#program to print the abbreivation of a month, given its number
def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec" #string all the same length
    n = eval(input("Enter a month number (1-12)")) #ask user to enter a number
    #compute starting position of month n in months
    pos = (n-1) * 3
    # Grab the appropriate slice from months
    monthAbbrev = months[pos:pos + 3]  #lengh of 3
    #print result
    print("The month abbreviation is ", monthAbbrev + ".")

main()
