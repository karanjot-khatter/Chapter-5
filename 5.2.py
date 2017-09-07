#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     29/08/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    gradeEntry = eval(input("Please enter the quiz score (0-5)"))
    grades = ["F", "F","D","C","B","A"]
    gradeStr = grades[gradeEntry]
    print("The grade:{0:1}".format(gradeEntry), "is equivalent to: {0:1}".format(gradeStr))
main()