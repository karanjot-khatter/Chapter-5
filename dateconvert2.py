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
#converts day month and years numbers into 2 date formats
def main():
    day,month,year = eval(input("enter day, month and year numbers: "))

    date1 = str(month) + "/" + str(day) + "/" + str(year)
    months = ["January", "Febuary", "March", "April",
     "May", "June", "July", "August", "September", "October",
     "November", "December"]

    monthStr = months[month-1]
    date2 = monthStr + " " + str(day) + ", " + str(year)

    print("The date is", date1, "or", date2 + ".")
main()