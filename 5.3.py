#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     30/08/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program accepts an exam score and prints out the corresponding grade")
    inputGrade = eval(input("Please enter an exam score (out of 100)"))
    if inputGrade <=100 and inputGrade>=90:
        print("If the input is:{0:3}".format(inputGrade), ".Then the exam score is: A")
    elif inputGrade >= 80 and inputGrade <90:
        print("If the input is:{0:3}".format(inputGrade), ".Then the exam score is: B")
    elif inputGrade >=70 and inputGrade <80:
        print("If the input is:{0:3}".format(inputGrade), ".Then the exam score is: C")
    elif inputGrade >=60 and inputGrade <70:
        print("If the input is:{0:3}".format(inputGrade), ".Then the exam score is: D")
    elif inputGrade <60 and inputGrade >=0:
        print("If the input is:{0:3}".format(inputGrade), ".Then the exam score is: F")
    else:
         print("This value is not between 0 - 100")
main()