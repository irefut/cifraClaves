# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:40:36 2023

@author: Irene

Cifrado de clave China:
    
    Ver: https://es.scribd.com/doc/310669075/Clave-China
    
    Los caracteres que no son reconocidos se quedan como un espacio
    en blanco y como caracteres extra, además de las letras del abecedario,
    están incluidos:
    -el espacio ' ' como /
    -las comillas '"'
    -el punto '.'
    -la coma ','
    -guión '-'
    
    Incluye la Ñ
    
    PD: Se le podrían agregar los signos ¿?¡! más adelante
"""
import turtle
from turtle import Turtle

def cerrar():
    try:    
        turtle.bye()   
    except turtle.Terminator:
        pass

def claveChina(Mensaje):
    
    turtle.title("Clave China")
    
    ColA =      ["o","ó","ö","p","q","r","s","t","u","ú","ü","v","w","x","y","z"]
    ColE =      ["e","é","f","g","h","o","ó","ö","p","q","r","s","t","u","ú","ü","v","w","x","y","z","i","í","j","k","l","m","n","ñ",]
    ColI =      ["o","ó","ö","p","q","r","s","t","a","á","b","c","d","i","í","j","k","l","m","n","ñ","u","ú","ü","v","w","x","y","z"]
    ColO =      ["e","é","f","g","h","o","ó","ö","p","q","r","s","t","u","ú","ü","v","w","x","y","z","i","í","j","k","l","m","n","ñ",]
    ColU =      ["u","ú","ü","v","w","x","y","z"]

    Fila2=      ["n","t","z","ñ"]
    Fila3=      ["c","g","k","q","w","d","h","l","r","x","m","s","y","n","t","z","ñ"]
    Fila4=      ["b","f","j","p","v","c","g","k","q","w","d","h","l","r","x","m","s","y","n","t","z","ñ"]
    Fila5=      ["d","h","l","r","x","m","s","y","n","t","z","ñ"]
    Fila6=      ["m","s","y","n","t","z","ñ"]
    Fila7=      ["ñ"]
    
    fontSize = 0.5
    
    def InitialiseTurtle(t):
        t.speed(0)
        t.hideturtle()
        t.pensize(3)
        t.color('black')
            
    def PenGoto(loc,t):
        t.penup()
        t.goto(loc)
        t.pendown()
    
    def CA(locx,locy,t):
        PenGoto((locx,locy),t)
        t.setheading(90)
        t.forward(80*fontSize)
    
    def F2(locx,locy,t):
        PenGoto((locx-23*fontSize,locy),t)
        t.setheading(0)
        t.forward(80*fontSize)
    
        
    def Guion(locx,locy,t):
        temp = t.pensize()
        draw.pensize(5*fontSize)
        PenGoto((locx+2,locy+12),t)
        t.setheading(0)
        t.forward(15)
        draw.pensize(temp)
        
    def Comillas(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx+5,locy+27),t)
        t.setheading(90-25)
        t.forward(12)
        PenGoto((locx+10,locy+27),t)
        t.setheading(90-25)
        t.forward(12)
        draw.pensize(temp)
        
    def Punto(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx+10,locy),draw)
        draw.pensize(8)
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
        PenGoto((locx,locy),t)
        t.setheading(90-30)
        t.forward(70*fontSize)
        
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
        if "colA" in mode:
            CA(locx,locy-5,draw)
        if "colE" in mode:
            CA(locx+5,locy-5,draw)
        if "colI" in mode:
            CA(locx+10,locy-5,draw)
        if "colO" in mode:
            CA(locx+15,locy-5,draw)
        if "colU" in mode:
            CA(locx+20,locy-5,draw)
        if "fila2" in mode:
            F2(locx,locy+27,draw)
        if "fila3" in mode:
            F2(locx,locy+22,draw)
        if "fila4" in mode:
            F2(locx,locy+17,draw)
        if "fila5" in mode:
            F2(locx,locy+12,draw)
        if "fila6" in mode:
            F2(locx,locy+7,draw)
        if "fila7" in mode:
            F2(locx,locy+2,draw)
        if "dobleDiagonal" in mode:
            DDiagonal(locx,locy,draw)
        if "simpleDiagonal" in mode:
            SDiagonal(locx,locy,draw)
        if "flecha" in mode:
            Flecha(locx+25,locy+10,draw)
    
    turtle.resetscreen()
    turtle.hideturtle()
    draw = Turtle()
    InitialiseTurtle(draw)
    
    #Cordenada inicial
    x = -340
    y = 240
    
    #Indica el inicio de la clave con una flecha
    Square("flecha", x, y)
    x += 110*fontSize
    
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
        if i in ColA:
            mode+="colA"
        if i in ColE:
            mode+="colE"
        if i in ColI:
            mode+="colI"
        if i in ColO:
            mode+="colO"
        if i in ColU:
            mode+="colU"
        if i in Fila2:
            mode+="fila2"
        if i in Fila3:
            mode+="fila3"
        if i in Fila4:
            mode+="fila4"
        if i in Fila5:
            mode+="fila5"
        if i in Fila6:
            mode+="fila6"
        if i in Fila7:
            mode+="fila7"
        if i in ["-"]:
            Guion(x,y,draw)
            
        Square(mode,x,y)
        x += 110*fontSize
        if x >= 300:
            x = -320
            y -= 110*fontSize

    turtle.Screen._update = False  
    turtle.Screen.mainloop()
           
            
#Mensaje = input("Introduce el mensaje para cifrar: ")
#claveChina("L-lBD  a, d. \" .ñ.ñ,ñ-ñ\"ñ")
#turtle.reset()