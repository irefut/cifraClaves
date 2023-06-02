# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:08:30 2023

@author: Irene

Codificando clave musical
"""

import turtle
from turtle import Turtle

def cerrar():
    try:    
        turtle.bye()   
    except turtle.Terminator:
        pass

def claveBailarin(Mensaje):
    
    turtle.title("Clave Musical")
    
    Uno =       ["1","a","á","j","r"]
    Dos =       ["2","b","k","s"]
    Tres =      ["3","c","l","t"]
    Cuatro =    ["4","d","m","u","ú","ü"]
    Cinco =     ["5","e","é","n","v"]
    Seis =      ["6","f","ñ","w"]
    Siete =     ["7","g","o","ó","ö","x"]
    Ocho =      ["8","h","p","y"]
    Nueve =     ["9","i","í","q","z"]
    Lleno =     ["r","s","t","u","ú","ü","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]
    Vacio =     ["a","á","b","c","d","e","é","f","g","h","i","í","j","k","l","m","n","ñ","o","ó","ö","p","q"]
    Izq =       ["j","k","l","m","n","ñ","o","ó","ö","p","q","1","2","3","4","5","6","7","8","9"]
    Der =       ["a","á","b","c","d","e","é","f","g","h","i","í","r","s","t","u","ú","ü","v","w","x","y","z"]
    Arriba =    ["a","á","b","c","d","e","é","f","g","h","i","r","s","t","u","ú","ü","v","w","x","y","z"]
    Abajo =     ["j","k","l","m","n","ñ","o","ó","ö","p","q","1","2","3","4","5","6","7","8","9"]
    
    
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
        
    def Guion(locx,locy,t):
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx-7,locy+15*fontSize),t)
        t.setheading(0)
        t.forward(15)
        draw.pensize(temp)   
       
    def Comillas(locx,locy,t):
        #Dibuja Comillas dobles
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+25),t)
        t.setheading(90-25)
        t.forward(18*fontSize)
        PenGoto((locx+5,locy+25),t)
        t.setheading(90-25)
        t.forward(18*fontSize)
        draw.pensize(temp)
        
    def Punto(locx,locy,t):
        temp = t.pensize()
        draw.pensize(3)
        PenGoto((locx,locy),draw)
        t.setheading(90)
        t.forward(49)
        draw.pensize(temp)
        
    def Coma(locx,locy,t):
        temp = t.pensize()
        PenGoto((locx,locy-20),draw)
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
    ### este sería el punto    
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
        
    def One(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy-5),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
        
    def Two(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
        
    def Three(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy+5),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
        
    def Four(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy+10),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
        
    def Five(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy+15),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
    
    def Six(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy+20),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
        
    def Seven(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy+25),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
    
    def Eight(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy+30),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
        
    def Nine(locx,locy,t,full):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy+35),draw)
        if full == True:  
            t.fillcolor("grey")
        else:
            t.fillcolor("white")
        draw.begin_fill()
        draw.circle(6)
        t.end_fill()
        draw.pensize(temp)
        
    def Stick(locx,locy,t,side,up):
        temp = t.pensize()
        draw.pensize(2)
        if side == "l":
            PenGoto((locx-5,locy),draw)
        else:
            PenGoto((locx+6,locy),draw)
        if up == True:
            t.setheading(90)
        else:
            t.setheading(270)
        t.forward(15)   
        draw.pensize(temp)
    
    def Pentagrama(locx,locy,t):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy),t)
        t.setheading(0)
        t.forward(23)
        PenGoto((locx,locy+12),t)
        t.setheading(0)
        t.forward(23)
        PenGoto((locx,locy+24),t)
        t.setheading(0)
        t.forward(23)
        PenGoto((locx,locy+36),t)
        t.setheading(0)
        t.forward(23)
        PenGoto((locx,locy+48),t)
        t.setheading(0)
        t.forward(23)
        draw.pensize(temp)
        
    def SolN(locx,locy,t):
        temp = t.pensize()
        draw.pensize(2)
        PenGoto((locx,locy),t)
        t.setheading(0)
        t.forward(50)
        PenGoto((locx,locy+12),t)
        t.setheading(0)
        t.forward(50)
        PenGoto((locx,locy+24),t)
        t.setheading(0)
        t.forward(50)
        PenGoto((locx,locy+36),t)
        t.setheading(0)
        t.forward(50)
        PenGoto((locx,locy+48),t)
        t.setheading(0)
        t.forward(50)
        alfa=100
        PenGoto((locx+15,locy+15),t)
        for x in range(31):
            t.setheading(0+alfa)
            if x<2:
                draw.pensize(2)
                t.forward(3)
                alfa-=21
            elif x<5:
                draw.pensize(3)
                t.forward(3)
                alfa-=22
            elif x<8:
                draw.pensize(5)
                t.forward(4)
                alfa-=22
            elif x<10:
                draw.pensize(4)
                t.forward(3)
                alfa-=22
            elif x<15:
                draw.pensize(3)
                t.forward(4)
                alfa-=18
            elif x<22:
                draw.pensize(3)
                t.forward(5)
                alfa-=20
            elif x<25:
                draw.pensize(3)
                t.forward(6)
                alfa+=20
                #t.stamp()
            elif x<29:
                draw.pensize(3)
                t.forward(5)
                alfa+=42
                #t.stamp()
            else:
                draw.pensize(3)
                t.forward(3)
                alfa+=30
        t.setheading(274)
        t.forward(50)
        t.setheading(240)
        t.forward(3)
        t.setheading(210)
        t.forward(3)
        t.setheading(180)
        t.forward(3)
        PenGoto((locx+13,locy-3),t)
        draw.pensize(15*fontSize)
        draw.forward(0.01)
        draw.pensize(temp)
        
    def Square(mode,locx,locy):
        Flag = False
        up = False
        side = "l"
        if "lleno" in mode:
            Flag = True  
        if "vacio" in mode:
            Flag = False
        if "arriba" in mode:
            up = True
        if "abajo" in mode:
            up = False
        if "izq" in mode:
            side = "l"
        if "der" in mode:
            side = "r"
        if "uno" in mode:
            Pentagrama(locx,locy,draw)
            One(locx,locy,draw,Flag)
            Stick(locx,locy,draw,side,up)
        if "dos" in mode:
            Pentagrama(locx,locy,draw)
            Two(locx,locy,draw,Flag)
            Stick(locx,locy+6,draw,side,up)
        if "tres" in mode:
            Pentagrama(locx,locy,draw)
            Three(locx,locy+2,draw,Flag)
            Stick(locx,locy+13,draw,side,up)
        if "cuatro" in mode:
            Pentagrama(locx,locy,draw)
            Four(locx,locy+2,draw,Flag)
            Stick(locx,locy+18,draw,side,up)
        if "cinco" in mode:
            Pentagrama(locx,locy,draw)
            Five(locx,locy+3,draw,Flag)
            Stick(locx,locy+25,draw,side,up)
        if "seis" in mode:
            Pentagrama(locx,locy,draw)
            Six(locx,locy+4,draw,Flag)
            Stick(locx,locy+30,draw,side,up)
        if "siete" in mode:
            Pentagrama(locx,locy,draw)
            Seven(locx,locy+6,draw,Flag)
            Stick(locx,locy+37,draw,side,up)
        if "ocho" in mode:
            Pentagrama(locx,locy,draw)
            Eight(locx,locy+6,draw,Flag)
            Stick(locx,locy+43,draw,side,up)
        if "nueve" in mode:
            Pentagrama(locx,locy,draw)
            Nine(locx,locy+8,draw,Flag)
            Stick(locx,locy+48,draw,side,up)
        if "punto" in mode:
            Pentagrama(locx,locy,draw)
            Punto(locx,locy,draw)
        
        if "dobleDiagonal" in mode:
            DDiagonal(locx,locy,draw)
        if "sol" in mode:
            SolN(locx,locy,draw)
    
    turtle.resetscreen()
    turtle.hideturtle()
    draw = Turtle()
    InitialiseTurtle(draw)
    
    #Cordenada inicial
    x = -330
    y = 220
    
    #Indica el inicio de la clave con una flecha
    Square("sol", x, y)
    x += 50
    
    for i in Mensaje:
        try:
            i = i.lower()
        except:
            None
        mode = ""
        if i in ['"']:
            Comillas(x,y,draw)
        if i in ['.']:
            mode += "punto"
        if i in [',']:
            Coma(x,y,draw)
        if i in ["-"]:
            Guion(x,y,draw)
        if i in [" "]:
            Pentagrama(x,y,draw)
        if i in Vacio:
            mode+="vacio"
        if i in Lleno:
            mode+="lleno"
        if i in Izq:
            mode+="izq"
        if i in Der:
            mode+="der"
        if i in Arriba:
            mode+="arriba"
        if i in Abajo:
            mode+="abajo"
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
        if i in Ocho:
            mode+="ocho"
        if i in Nueve:
            mode+="nueve"
        
                       
        Square(mode,x,y)
        x += 23
        if x >= 300:
            x = -320
            y -= 160*fontSize
    #turtle.clearstamps()
    #turtle.done()
    turtle.Screen._update = False  
    turtle.Screen.mainloop()
    turtle.Screen().exitonclick()
           
            
#Mensaje = input("Introduce el mensaje para cifrar: ")
claveBailarin("gru.po scout")