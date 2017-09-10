#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     09/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():
    print("This program to plot a horizontal bar chart of student exam scores")

    #input
    fileName = input("Enter the file name:") #escores.txt
    inFile = open(fileName, "r")
    line = inFile.readlines()

    #get number of students from file - first line
    students = int(line[0])

    #create windows
    win = GraphWin("Student's exams scores", 500, 350)
    win.setCoords (0,0,10,14)
    win.setBackground("white")

    #Access the information in the file - starting form the first line.
    scores = []
    names = []
    for item in line[1:]:
      scores += [int(item.split()[1])] #second is the score
      names += [item.split()[0]] #first is the name

    #initial rectangle from first on the list
    rect = Rectangle(Point(3,2), Point(3 + 0.05 * scores[0], 10/(students)))
    rect.setFill("green")
    rect.draw(win)

    #inital name from first on the list - next to rectangle
    text = Text(Point(1.5, 5 / students + 1), names[0])
    text.setStyle("bold")
    text.setSize(10)
    text.draw(win)

    #rectangles for other bars
    for i in range(students-1):
      rect = Rectangle(Point(3, rect.getP1().getY() + 10/students), Point(3 + 0.05 * scores[i+1], rect.getP2().getY() + 10/students))
      rect.setFill("green")
      rect.draw(win)

    #Create name next to bars
      text1 = Text(Point(1.5, (rect.getP1().getY() + rect.getP2().getY()) / 2), names[i + 1])
      text1.setStyle("bold")
      text1.setSize(10)
      text1.draw(win)

    #wait for mouse click
    win.getMouse()
    win.close()
main()