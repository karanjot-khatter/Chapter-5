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
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("Enter amount of columns"))
    #how many times it will print - from learners choice.
    print("{0:4}".format("Index"), "{0:8}".format(x), "{0:12}".format(y))
    print("---------------------------")
    for i in range(n):
        x = 3.9 * (x - x * x)
        y = 3.9 * (y - y * y)
        #if number between 0 and 10 - 6d.p
        print( "{0:5}".format(i+1),"{0:10.6f} {0:10.6f}" .format(x, y))


main()

