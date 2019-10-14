# Turtle Graphics: Repeating Squares
# 10/12/2019
# CTI-110-0007 P4T1 Turtle Graphic
# Steven Powers



# This program draws a design using repeated squares.
import turtle

# Implementation of drawSquare method
# which draws 100 square
def drawSquare():
    #Iterate the loop
    for each in range (100):
        #turtle.backward() method
        #which moves in backward direction the given distance
        turtle.backward(each+(each*2))
        #turtle.right() method
        #which turns the pointed to given agle in the square
        turtle.right(90)
        turtle.backward(each+(each*2))
        turtle.right(90)
        turtle.backward(each+(each*2))
        turtle.right(90)
        turtle.backward(each+(each*2))
        turtle.right(90)

#call drawSquare method
drawSquare()





