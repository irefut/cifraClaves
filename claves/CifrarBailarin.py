# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:57:20 2023

@author: Irene

Cifrado de clave bailarín

Cambia letra por un muñequito ver:
    https://es.scribd.com/doc/310011525/Clave-Bailarin#
    
El punto(.) sería una diagonal simple
"""

import turtle
from turtle import Turtle

def claveBailarin(Mensaje):
    
    turtle.title("Clave Bailarín")
    
    CbzUp =     ["a","á","b","c","d","e","é","f","h","i","í","j","l","m","n","o","ó","ö","p","q","r","s","u","ú","ü","v","w","x","y","z"," "]
    CbzDwn =    ["g","k","t"]
    LBrzUp =    ["a","á","c","e","é","f","h","m","o","ó","ö","r","w","i","í"]
    LBrzDwn =   ["z"," "]
    LBrzDwnHD = ["g","t"]  
    RBrzUp =    ["a","á","e","é","f","h","i","í","m","n","o","ö","ó","r","w","y"]
    RBrzDwn =   ["z"]
    RBrzDwnHD = ["g","k","t"]
    BrzsL =     ["l"]
    LBrzN =     ["n"]
    BrzsQ =     ["q"]
    BrzsS =     ["s"]
    BrzsPlano = ["u","ú","ü","x"]
    LPrnEst =   ["a","á","p","e","é","j","r","x"]
    LPrnPlEst = ["h","z"," "]
    LPrnDbl =   ["b","c","f","l","m","o","ó","ö","q","s","u","ú","ü","y"]
    LPrnArr =   ["d","i","í"]
    LPrnAb =    ["v","w"]
    PrnsN =     ["n"]
    RPrnEst =   ["e","é","f","j","x"]
    RPrnPlEst = ["h","z"," "]
    RPrnDbl =   ["a","á","b","c","l","m","n","q","s","u","ú","ü","y"]
    RPrnArr =   ["r","v","w"]
    RPrnAb =    ["d","i","í","o","ó","ö","p"]
    PrnsArr =   ["g","k","t"]
    Bandera =   [" "]
    
    
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
        
    def HeadUp(locx,locy,t):
        #Cabeza y cuerpo
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+19),t)
        t.setheading(270)
        t.forward(25)
        PenGoto((locx-7,locy+26),t)
        draw.circle(7)
        draw.pensize(temp)
        
    def HeadDwn(locx,locy,t):
        #Cabeza y cuerpo al revés
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+17),t)
        t.setheading(270)
        t.forward(23)
        PenGoto((locx-7,locy-15),t)
        draw.circle(7)
        draw.pensize(temp)
        
    def Flag(locx,locy,t):############
        #Brazito con bandera
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(330)
        t.forward(25)
        t.setheading(240)
        t.forward(12)
        t.setheading(150)
        t.forward(12)
        t.setheading(60)
        t.forward(12)
        t.setheading(285)
        t.forward(15)
        t.setheading(65)
        t.forward(8)
        t.setheading(150)
        t.forward(6)
        t.setheading(300)
        t.forward(6)
        draw.pensize(temp)
        
    def LArmUp(locx,locy,t):
        #brazo izquierdo estirado arriab
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+10),t)
        t.setheading(135)
        t.forward(15)
        draw.pensize(temp)
        
    def LArmDwn(locx,locy,t):
        #Brazo izq estirado hacia abajo
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(215)
        t.forward(15)
        draw.pensize(temp)
        
    def LArmDwnHD(locx,locy,t):
        #Brazo izq hacia abajo pero con muñequito de cabeza
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+5),t)
        t.setheading(215)
        t.forward(15)
        draw.pensize(temp)
        
    def RArmDwnHD(locx,locy,t):
        #Brazo der hacia abajo pero con muñequito de cabeza
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+5),t)
        t.setheading(320)
        t.forward(15)
        draw.pensize(temp)
        
    def RArmUp(locx,locy,t):
        #brazo derecho estirado arriab
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+10),t)
        t.setheading(45)
        t.forward(15)
        draw.pensize(temp)
        
    def RArmDwn(locx,locy,t):
        #brazo derecho estirado hacia abajo
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(325)
        t.forward(15)
        draw.pensize(temp)
        
    def ArmsL(locx,locy,t):
        #brazos de L
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(0)
        t.forward(15)
        t.setheading(230)
        t.forward(15)
        PenGoto((locx,locy+12),t)
        t.setheading(180)
        t.forward(12)
        t.setheading(120)
        t.forward(12)
        draw.pensize(temp)
        
    def LArmN(locx,locy,t):############
        #Brazo izq de N
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(210)
        t.forward(13)
        t.setheading(320)
        t.forward(12)
        draw.pensize(temp)
        
    def ArmsQ(locx,locy,t):
        #Brazos de Q
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(25)
        t.forward(13)
        t.setheading(80)
        t.forward(6)
        PenGoto((locx,locy+12),t)
        t.setheading(205)
        t.forward(13)
        t.setheading(100)
        t.forward(6)
        draw.pensize(temp)
        
    def ArmsS(locx,locy,t):############
        #Brazos de S
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(340)
        t.forward(13)
        t.setheading(80)
        t.forward(6)
        PenGoto((locx,locy+12),t)
        t.setheading(160)
        t.forward(13)
        t.setheading(100)
        t.forward(6)
        draw.pensize(temp)
        
    def ArmsPlano(locx,locy,t):############
        #Brazos planos
        temp = t.pensize()
        draw.pensize(2.5)
        PenGoto((locx,locy+12),t)
        t.setheading(0)
        t.forward(13)
        t.setheading(80)
        t.forward(6)
        PenGoto((locx,locy+12),t)
        t.setheading(180)
        t.forward(13)
        t.setheading(100)
        t.forward(6)
        draw.pensize(temp)
        
    def LLegEstirada(locx,locy,t):
        temp = t.pensize()
        #Pierna izquierda estirada
        PenGoto((locx,locy-7),t)
        t.setheading(230)
        t.forward(18)
        t.setheading(150)
        t.forward(6)
        draw.pensize(temp)
        
    def LLegEstiradaPl(locx,locy,t):
        temp = t.pensize()
        #Pierna izquierda estirada plano el pie
        PenGoto((locx,locy-7),t)
        t.setheading(240)
        t.forward(18)
        t.setheading(180)
        t.forward(6)
        draw.pensize(temp)
        
    def LLegBend(locx,locy,t):
        temp = t.pensize()
        #Pierna izquierda doblada
        PenGoto((locx,locy-7),t)
        t.setheading(210)
        t.forward(10)
        t.setheading(290)
        t.forward(10)
        t.setheading(180)
        t.forward(6)
        draw.pensize(temp)
        
    def LLegUp(locx,locy,t):
        temp = t.pensize()
        #Pierna izquierda estirada arriba
        PenGoto((locx,locy-7),t)
        t.setheading(180)
        t.forward(12)
        t.setheading(90)
        t.forward(6)
        draw.pensize(temp)
        
    def LLegDwn(locx,locy,t):
        temp = t.pensize()
        #Pierna izquierda hacia abajo
        PenGoto((locx,locy-7),t)
        t.setheading(270)
        t.forward(14)
        t.setheading(180)
        t.forward(6)
        draw.pensize(temp)
        
    def LegsN(locx,locy,t):##########
        temp = t.pensize()
        #Piernas de N
        PenGoto((locx,locy-7),t)
        t.setheading(170)
        t.forward(12)
        t.setheading(280)
        t.forward(12)
        t.setheading(190)
        t.forward(6)
        draw.pensize(temp)
        
    def RLegEstirada(locx,locy,t):
        temp = t.pensize()
        #Pierna derecha estirada
        PenGoto((locx,locy-7),t)
        t.setheading(310)
        t.forward(18)
        t.setheading(45)
        t.forward(6)
        draw.pensize(temp)
        
    def RLegEstiradaPl(locx,locy,t):
        temp = t.pensize()
        #Pierna der estirada pie plano
        PenGoto((locx,locy-7),t)
        t.setheading(300)
        t.forward(18)
        t.setheading(0)
        t.forward(6)
        draw.pensize(temp)
        
    def RLegUp(locx,locy,t):###################
        temp = t.pensize()
        #Pierna der estirada arriba
        PenGoto((locx,locy-7),t)
        t.setheading(0)
        t.forward(15)
        t.setheading(90)
        t.forward(6)
        draw.pensize(temp)
        
    def RLegDwn(locx,locy,t):
        temp = t.pensize()
        #Pierna der hacia abajo
        PenGoto((locx,locy-7),t)
        t.setheading(270)
        t.forward(14)
        t.setheading(0)
        t.forward(6)
        draw.pensize(temp)
        
    def LegsUp(locx,locy,t):
        temp = t.pensize()
        #Piernas cuando está de cabeza
        PenGoto((locx,locy+16),t)
        t.setheading(120)
        t.forward(18)
        t.setheading(220)
        t.forward(6)
        PenGoto((locx,locy+16),t)
        t.setheading(60)
        t.forward(18)
        t.setheading(320)
        t.forward(6)
        draw.pensize(temp)
        
    def RLegBend(locx,locy,t):
        temp = t.pensize()
        #Pierna derecha recogida
        PenGoto((locx,locy-7),t)
        t.setheading(330)
        t.forward(10)
        t.setheading(240)
        t.forward(10)
        t.setheading(0)
        t.forward(6)
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
        PenGoto((locx,locy-20),draw)
        draw.pensize(15*fontSize)
        draw.forward(0.01)
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
        if "cbzUp" in mode:
            HeadUp(locx,locy,draw)
        if "cbzDwn" in mode:
            HeadDwn(locx,locy,draw)
        if "lBrzUp" in mode:
            LArmUp(locx,locy,draw)
        if "lBrzDwn" in mode:
            LArmDwn(locx,locy,draw)
        if "lBrzDwHD" in mode:
            LArmDwnHD(locx,locy,draw)
        if "rBrzUp" in mode:
            RArmUp(locx,locy,draw)
        if "rBrzDwn" in mode:
            RArmDwn(locx,locy,draw)
        if "rBrzDwHD" in mode:
            RArmDwnHD(locx,locy,draw)
        if "lBrzN" in mode:
            LArmN(locx,locy,draw)
        if "brzL" in mode:
            ArmsL(locx,locy,draw)
        if "brzsQ" in mode:
            ArmsQ(locx,locy,draw)
        if "brzsS" in mode:
            ArmsS(locx,locy,draw)
        if "brzsPlano" in mode:
            ArmsPlano(locx,locy,draw)
        if "lPrnEst" in mode:
            LLegEstirada(locx,locy,draw)
        if "lPrnDbl" in mode:
            LLegBend(locx,locy,draw)
        if "lPrnArr" in mode:
            LLegUp(locx,locy,draw)
        if "lPrnAb" in mode:
            LLegDwn(locx,locy,draw)
        if "prnsN" in mode:
            LegsN(locx,locy,draw)
        if "rPrnEst" in mode:
            RLegEstirada(locx,locy,draw)
        if "rPrnPlEst" in mode:
            RLegEstiradaPl(locx,locy,draw)
        if "lPrnPlEst" in mode:
            LLegEstiradaPl(locx,locy,draw)
        if "rPrnDbl" in mode:
            RLegBend(locx,locy,draw)
        if "rPrnArr" in mode:
            RLegUp(locx,locy,draw)
        if "rPrnAb" in mode:
            RLegDwn(locx,locy,draw)
        if "prnsArr" in mode:
            LegsUp(locx,locy,draw)
        if "bandera" in mode:
            Flag(locx,locy,draw)
        if "flecha" in mode:
            Flecha(locx+25,locy+5,draw)
    
    turtle.resetscreen()
    turtle.hideturtle()
    draw = Turtle()
    InitialiseTurtle(draw)
    
    #Cordenada inicial
    x = -340
    y = 245
    
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
        if i in Bandera:
            mode+="bandera"
        if i in CbzUp:
            mode+="cbzUp"
        if i in CbzDwn:
            mode+="cbzDwn"
        if i in LBrzUp:
            mode+="lBrzUp"
        if i in LBrzDwn:
            mode+="lBrzDwn"
        if i in LBrzDwnHD:
            mode+="lBrzDwHD"
        if i in RBrzUp:
            mode+="rBrzUp"
        if i in RBrzDwn:
            mode+="rBrzDwn"
        if i in RBrzDwnHD:
            mode+="rBrzDwHD"
        if i in LBrzN:
            mode+="lBrzN "
        if i in ["-"]:
            Guion(x,y,draw)
        if i in BrzsL:
            mode+="brzL"
        if i in BrzsQ:
            mode+="brzsQ"
        if i in BrzsS:
            mode+="brzsS"
        if i in BrzsPlano:
            mode+="brzsPlano"
        if i in LPrnEst:
            mode+="lPrnEst"
        if i in RPrnPlEst:
            mode+="rPrnPlEst"
        if i in LPrnPlEst:
            mode+="lPrnPlEst"
        if i in LPrnDbl:
            mode+="lPrnDbl"
        if i in LPrnArr:
            mode+="lPrnArr"
        if i in LPrnAb:
            mode+="lPrnAb"
        if i in PrnsN:
            mode+="prnsN"
        if i in RPrnEst:
            mode+="rPrnEst"
        if i in RPrnDbl:
            mode+="rPrnDbl"
        if i in RPrnArr:
            mode+="rPrnArr"
        if i in RPrnAb:
            mode+="rPrnAb"
        if i in PrnsArr:
            mode+="prnsArr"
      
            
        Square(mode,x,y)
        x += 80*fontSize
        if x >= 300:
            x = -320
            y -= 160*fontSize
    #turtle.clearstamps()
    #turtle.done()
    turtle.Screen._update = False  
    turtle.Screen.mainloop()
    turtle.Screen().exitonclick()
           
            
#Mensaje = input("Introduce el mensaje para cifrar: ")
#claveBailarin("L-lBD  a, d. \" .")