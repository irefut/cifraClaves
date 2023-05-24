# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:21:33 2023

@author: Irene
"""
# Python program to user input pattern
# using Turtle Programming
import turtle   #Outside_In
import time
import random

turtle.title("Welcome to the turtle zoo!")

print ("This program draws shapes based on the number you enter in a uniform pattern.")
#num_str = input("Enter the side number of the shape you want to draw: ")

def estees(num_str):
    if num_str.isdigit():
        squares = int(num_str)
     
    angle = 180 - 180*(squares-2)/squares
     
    turtle.up
    turtle.hideturtle()
    
    x = 0
    y = 0
    turtle.setpos(x, y)
         
    numshapes = 4
    for x in range(numshapes):
        turtle.color(random.random(), random.random(), random.random())
        x += 5
        y += 5
        turtle.forward(x)
        turtle.left(y)
        for i in range(squares):
            turtle.begin_fill()
            turtle.down()
            turtle.forward(40)
            turtle.left(angle)
            turtle.forward(40)
            print (turtle.pos())
            turtle.up()
            turtle.end_fill()
     
    time.sleep(1)
    x = 0
    y = 0
    turtle.setpos(x, y)
        

    
def borrar():
    turtle.clear()

estees("3")
borrar()
estees('4')

