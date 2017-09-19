#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     10/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def main():
    print("This program will draw a quiz score histogram") #qscores.txt

    #input
    fileName = input("Please enter the filename:")
    inFile = open(fileName,"r")
    line = inFile.readlines()

    #create windows
    win = GraphWin("Quiz scores", 500, 300)
    win.setCoords (0,0,10,14)
    win.setBackground("white")

    #Title
    text2 = Text(Point(5, 10),"Histogram")
    text2.setStyle("bold")
    text2.setSize(10)
    text2.draw(win)

    #Access the information in the file - starting form the first line.

    totalScore = []
    for item in line:
        totalScore += [int(item.split()[0])] #without split - 10 won't appear
        totalScores = totalScore.count(0), totalScore.count(1), totalScore.count(2), totalScore.count(3),totalScore.count(4), totalScore.count(5),totalScore.count(6), totalScore.count(7),totalScore.count(8), totalScore.count(9), totalScore.count(10)
        #The above need to be in the for loop, otherwise does not count all lines

    #inital rectangle
    rect = Rectangle(Point(0.5,3.5), Point(1 + 3 * totalScore[0], 2.5))
    rect.setFill("green")
    rect.draw(win)

    #inital name from first on the list - below to rectangle
    text = Text(Point(0.75, 1.75),[0])
    text.setStyle("bold")
    text.setSize(10)
    text.draw(win)

    #rectangles for other bars
    for i in range(10):
      rect = Rectangle(Point(rect.getP1().getX() + 1, 2.5), Point(rect.getP2().getX() + 1, 2.5 + 1 *totalScores[i+1]))
      rect.setFill("green")
      rect.draw(win)

      #Create x axis 1-10
     # text1 = Text(Point(1.75, (rect.getP1().getX() + rect.getP2().getX()) / 2), [i + 1])
      text1 = Text(Point(rect.getP1().getX() / 2 + rect.getP2().getX() / 2, 1.75), [i+1])
      text1.setStyle("bold")
      text1.setSize(10)
      text1.draw(win)



    #wait for mouse click
    win.getMouse()
    win.close()
main()