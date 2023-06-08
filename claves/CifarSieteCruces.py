# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:28:27 2023

@author: Irene

Cifrar clave siete cruces
"""

import turtle
from turtle import Turtle

def cerrar():
    try:    
        turtle.bye()   
    except turtle.Terminator:
        pass

def claveSieteCruces(Mensaje):
    
    turtle.title("Clave Siete Cruces")
    
    #todo abcdario ["a","á","b","c","d","e","é","f","g","h","i","í","j","k","l""m","n","ñ","o","ó","ö","p","q","r","s","t","u","ú","ü","v","w","x","y","z"]

    Arriba =    ["a","á","e","é","i","í","m","p","t","x"]
    Derecha =   ["b","f","j","n","q","u","ú","ü","y"]
    Abajo =     ["c","g","k","ñ","r","v","z"]
    Izquierda = ["d","h","l","o","ó","ö","s","w"," "]
    
    Uno =       ["a","á","b","c","d"]
    Dos =       ["e","é","f","g","h"]
    Tres =      ["i","í","j","k","l"]
    Cuatro =    ["m","n","ñ","o","ó","ö"]
    Cinco =     ["p","q","r","s"]
    Seis =      ["t","u","ú","ü","v","w"]
    Siete =     ["x","y","z"," "]
    
    fontSize = 0.8
    
    def InitialiseTurtle(t):
        t.speed(0)
        t.hideturtle()
        t.pensize(3)
        t.color('black')
            
    def PenGoto(loc,t):
        t.penup()
        t.goto(loc)
        t.pendown()
    
    def Left(locx,locy,t):
        PenGoto((locx+10,locy-12),t)
        t.setheading(205+180)
        t.forward(40)
        t.setheading(330+180)
        t.forward(40)
    
    def Right(locx,locy,t):
        PenGoto((locx+40,locy+25),t)
        t.setheading(205)
        t.forward(40)
        t.setheading(330)
        t.forward(40)
    
    def Bottom(locx,locy,t):
        PenGoto((locx+45,locy-12),t)
        t.setheading(300+180)
        t.forward(40)
        t.setheading(58+180)
        t.forward(40)
    
    def Top(locx,locy,t):
        PenGoto((locx,locy+30*fontSize),t)
        t.setheading(300)
        t.forward(40)
        t.setheading(58)
        t.forward(40)
        
    def Guion(locx,locy,t):
        temp = t.pensize()
        draw.pensize(5*fontSize)
        PenGoto((locx+15,locy+10*fontSize),t)
        t.setheading(0)
        t.forward(20*fontSize)
        draw.pensize(temp)
        
    def Comillas(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx+25,locy+15*fontSize),t)
        draw.pensize(4*fontSize)
        t.setheading(90-25)
        t.forward(18*fontSize)
        PenGoto((locx+20,locy+15*fontSize),t)
        t.setheading(90-25)
        t.forward(18*fontSize)
        draw.pensize(temp)
        
    def Punto(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx+25*fontSize,locy+5*fontSize),draw)
        draw.pensize(12*fontSize)
        draw.forward(0.01)
        draw.pensize(temp)
        
    def Coma(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx+25*fontSize,locy+5*fontSize),draw)
        draw.pensize(10*fontSize)
        draw.forward(0.01)
        t.setheading(90)
        draw.pensize(9*fontSize)
        draw.back(3)
        t.setheading(90-20)
        draw.pensize(7*fontSize)
        draw.back(3)
        t.setheading(90-35)
        draw.pensize(5.5*fontSize)
        draw.back(3)
        t.setheading(90-60)
        draw.pensize(4*fontSize)
        draw.back(3)
        draw.pensize(temp)
    
    def DDiagonal(locx,locy,t):
        PenGoto((locx,locy),t)
        t.setheading(90-30)
        t.forward(44.72*fontSize)
        PenGoto((locx+14*fontSize,locy),t)
        t.setheading(90-30)
        t.forward(44.72*fontSize)
        
    def SDiagonal(locx,locy,t):
        PenGoto((locx+15,locy-8),t)
        t.setheading(90-30)
        t.forward(44.72*fontSize)
        
    def Circle(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx+25*fontSize,locy+15*fontSize),draw)
        draw.pensize(10*fontSize)
        draw.forward(0.01)
        draw.pensize(temp)
        
    def Flecha(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx,locy),t)
        draw.pensize(5*fontSize)
        t.setheading(90-45)
        t.forward(15*fontSize)
        t.setheading(-45)
        t.back(15*fontSize) 
        t.setheading(-45)
        t.forward(15*fontSize)
        t.setheading(0)
        t.back(35*fontSize)
        draw.pensize(temp)
        
    def One(locx,locy,t):
        PenGoto((locx+19,locy+5),t)
        t.setheading(90)
        t.forward(15)
        
    def Two(locx,locy,t):
        PenGoto((locx+15,locy+15),t)
        alfa = 70
        for i in range(7):
            t.setheading(0+alfa)
            t.forward(2)
            alfa -=22
        t.setheading(230)
        t.forward(14)
        t.setheading(0)
        t.forward(10)
        
    def Three(locx,locy,t):
        PenGoto((locx+15,locy+17),t)
        alfa = 70
        for i in range(8):
            t.setheading(0+alfa)
            t.forward(3)
            alfa -=37
        alfa = 0
        for i in range(8):
            t.setheading(0+alfa)
            t.forward(3)
            alfa -=35
        
    def Four(locx,locy,t):
        PenGoto((locx+15,locy+20),t)
        t.setheading(270)
        t.forward(8)
        t.setheading(0)
        t.forward(8)
        t.setheading(90)
        t.forward(8)
        t.setheading(270)
        t.forward(16)
        
    def Five(locx,locy,t):
        PenGoto((locx+25,locy+20),t)
        t.setheading(180)
        t.forward(8)
        t.setheading(270)
        t.forward(8)
        alfa = 25
        for i in range(8):
            t.setheading(0+alfa)
            t.forward(3)
            alfa -=37

    def Six(locx,locy,t):
        PenGoto((locx+19,locy+11),t)
        alfa = 55
        for x in range(14):
            t.setheading(0+alfa)
            if x<5:
                t.forward(3)
                alfa-=40
            elif x<10:
                t.forward(4)
                alfa-=30
            else:
                t.forward(4)
                alfa-=18
        
    def Seven(locx,locy,t):
        PenGoto((locx+15,locy+17),t)
        t.setheading(0)
        t.forward(10)
        t.setheading(240)
        t.forward(15)
        
    def Square(mode,locx,locy):
        tempx = locx
        tempy = locy
        if "izq" in mode:
            Left(locx,locy,draw)
            tempy = locy-6
        if "der" in mode:
            Right(locx,locy,draw)
            tempx = locx+13
            tempy = locy-6
        if "abajo" in mode:
            Bottom(locx,locy,draw)
            tempx = locx+5
            tempy = locy-15
        if "arriba" in mode:
            Top(locx,locy,draw)
        if "dobleDiagonal" in mode:
            DDiagonal(locx,locy,draw)
        if "simpleDiagonal" in mode:
            SDiagonal(locx,locy,draw)
        if "flecha" in mode:
            Flecha(locx+25,locy+5,draw)
        if "uno" in mode:
            One(tempx,tempy,draw)
        if "dos" in mode:
            Two(tempx,tempy,draw)
        if "tres" in mode:
            Three(tempx,tempy,draw)
        if "cuatro" in mode:
            Four(tempx,tempy,draw)
        if "cinco" in mode:
            Five(tempx,tempy,draw)
        if "seis" in mode:
            Six(tempx,tempy,draw)
        if "siete" in mode:
            Seven(tempx,tempy,draw)
    
    turtle.resetscreen()
    turtle.hideturtle()
    draw = Turtle()
    InitialiseTurtle(draw)
    
    #Cordenada inicial
    x = -320
    y = 240
    
    #Indica el inicio de la clave con una flecha
    Square("flecha", x, y)
    x += 60*fontSize
    
    for i in Mensaje:
        try:
            i = i.lower()
        except:
            None
        mode = ""
        if i in ['"']:
            Comillas(x,y,draw)
        if i in ['.']:
            mode+="simpleDiagonal"
        if i in [',']:
            Coma(x,y,draw)
        if i in Derecha:
            mode+="der"
        if i in Izquierda:
            mode+="izq"
        if i in Abajo:
            mode+="abajo"
        if i in Arriba:
            mode+="arriba"
        if i in Uno:
            mode+="uno"
        if i in Dos:
            mode+="dos"
        if i in Tres:
            mode+="tres"
        if i in Cuatro:
            mode+="cuatro"
        if i in Cinco:
            mode+="cinco"
        if i in Seis:
            mode+="seis"
        if i in Siete:
            mode+="siete"
        if i in ["-"]:
            Guion(x,y,draw)
            
        Square(mode,x,y)
        x += 60*fontSize
        if x >= 300:
            x = -320
            y -= 60*fontSize
    #turtle.clearstamps()
    #turtle.done()
    turtle.Screen._update = False  
    turtle.Screen.mainloop()
    turtle.Screen().exitonclick()
           
            
#Mensaje = input("Introduce el mensaje para cifrar: ")
#claveSieteCruces("ser scout") # ijkl mnño pqrs tuvw xyz
