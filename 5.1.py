#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     07/06/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#string formatting method

def main():
    day,month,year = eval(input("enter day, month and year numbers: "))

    date1 = str(day) + "/" + str(month) + "/" + str(year)

    months = ["January", "Febuary", "March", "April",
     "May", "June", "July", "August", "September", "October",
     "November", "December"]

    monthStr = months[month-1]
    date2 = "{0:3}".format(str(day)) + "{0:9}".format(monthStr) +  str(year)
#8 characters because month is less than that.

    print("The Date is: {0:<5}".format(date1), "or", date2 + ".")

main()