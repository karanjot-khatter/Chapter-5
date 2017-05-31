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
#convert a date in form "mm/dd/yyyy" to "month day, year"
def main():
    #get the date
    dateStr = input("Enter a date (mm/dd/yy):")

    #split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    #convert MonthStr to month name
    months = ["January", "Febuary", "March", "April",
     "May", "June", "July", "August", "September", "October",
     "November", "December"]

    monthStr = months[int(monthStr)- 1]

    #output result in month day, year formaat
    print("The converted date is: ", monthStr, dayStr + ",", yearStr)

main()