#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     07/09/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program calculates the average word length in a sentence") #e.g. yo yo yo would be 2 - becauses theres 2 characters each word
    sentence = input("Enter a sentence:")
    words = sentence.split() #splits sentence
    average = sum(len(word) for word in words) / len(words) #len = number of items in a list
    print(average)
main()