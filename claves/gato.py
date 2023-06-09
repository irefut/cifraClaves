# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:55:20 2023

@author: Irene
"""

from turtle import Turtle

Arriba =    ["j","k","l","m","n","ñ","o","ó","p","q","r","s","t","u","ú","v","w","x","y","z"]
Abajo =     ["a","á","b","c","d","e","é","f","g","h","i","í","j","k","l","m","n","ñ","o","ó","p","q"]
Derecha =   ["a","á","b","c","d","e","é","f","j","k","l","m","n","ñ","r","s","t","u","ú","v","w"]
Izquierda = ["d","e","é","f","g","h","i","í","m","n","ñ","o","ó","p","q","u","ú","v","w","x","y","z"]
DotDer =    ["c","f","i","í","l","ñ","q","t","w","z"]
DotIzq =    ["a","á","d","g","j","m","o","ó","r","u","ú","x"]
DotC =      ["b","e","é","h","k","n","p","s","v","y"]

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
    PenGoto((locx,locy),t)
    t.setheading(90)
    t.forward(30*fontSize)

def Right(locx,locy,t):
    PenGoto((locx+50*fontSize,locy),t)
    t.setheading(90)
    t.forward(30*fontSize)

def Bottom(locx,locy,t):
    PenGoto((locx,locy),t)
    t.setheading(0)
    t.forward(50*fontSize)

def Top(locx,locy,t):
    PenGoto((locx,locy+30*fontSize),t)
    t.setheading(0)
    t.forward(50*fontSize)
    
def Guion(locx,locy,t):
    temp = t.pensize()
    draw.pensize(5*fontSize)
    PenGoto((locx+10,locy+15*fontSize),t)
    t.setheading(0)
    t.forward(20*fontSize)
    draw.pensize(temp)
    
def Comillas(locx,locy,t):
    temp = t.pensize()
    PenGoto((locx+15,locy+25*fontSize),t)
    draw.pensize(4*fontSize)
    t.setheading(90-25)
    t.forward(18*fontSize)
    PenGoto((locx+20,locy+25*fontSize),t)
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
    PenGoto((locx+8,locy),t)
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
    
def Square(mode,locx,locy):
    if "izq" in mode:
        Left(locx,locy,draw)
    if "der" in mode:
        Right(locx,locy,draw)
    if "abajo" in mode:
        Bottom(locx,locy,draw)
    if "arriba" in mode:
        Top(locx,locy,draw)
    if "dobleDiagonal" in mode:
        DDiagonal(locx,locy,draw)
    if "simpleDiagonal" in mode:
        SDiagonal(locx,locy,draw)
    if "flecha" in mode:
        Flecha(locx+25,locy+5,draw)

        
draw = Turtle()
InitialiseTurtle(draw)

#Cordenada inicial
x = -320
y = 240

Mensaje = input("Introduce el mensaje para cifrar: ")

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
        Punto(x,y,draw)
    if i in [',']:
        Coma(x,y,draw)
    if i in [" "]:
        mode+="simpleDiagonal"
    if i in Derecha:
        mode+="der"
    if i in Izquierda:
        mode+="izq"
    if i in Abajo:
        mode+="abajo"
    if i in Arriba:
        mode+="arriba"
    if i in DotDer:
        Circle(x+12,y,draw)
    if i in DotIzq:
        Circle(x-12,y,draw)
    if i in ["-"]:
        Guion(x,y,draw)
    if i in DotC:
        Circle(x,y,draw)

    Square(mode,x,y)
    x += 60*fontSize
    if x >= 300:
        x = -320
        y -= 60*fontSize


def claveGato(texto):
    mensajecifrado = ""
    mensajecifrado = mensajecifrado + texto + '5'
    return mensajecifrado

original = input("Introduce el mensaje para cifrar: ")
gato = claveGato(original)
print(gato)

