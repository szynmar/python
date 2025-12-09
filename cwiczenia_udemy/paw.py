# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 01:26:31 2025

@author: Ala
"""

import turtle

n = 12
kat = 360 / n

turtle.speed(0)
turtle.left(90)
turtle.right(kat)

for i in range(n):
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.backward(170)
    turtle.right(kat)

turtle.left(kat)
turtle.right(90)
turtle.pendown()
# turtle.speed(1)

minBokKw = 10
n=5
koloryL=["red", "green", "blue", "yellow", "orange", "purple"]

while n > 0:
    turtle.fillcolor(koloryL[n])
    turtle.begin_fill()
    turtle.forward(n * minBokKw)
    turtle.left(90)
    turtle.forward(n * minBokKw)
    turtle.left(90)
    turtle.forward(n * minBokKw)
    turtle.left(90)
    turtle.forward(n * minBokKw)
    turtle.left(90)
    n -= 1
    turtle.end_fill()

turtle.right(235)
n = 5
while n > 0:
    turtle.fillcolor(koloryL[n])
    turtle.begin_fill()
    turtle.circle(n*minBokKw)
    turtle.end_fill()
    n -= 1

 
#turtle.hideturtle()
turtle.mainloop()