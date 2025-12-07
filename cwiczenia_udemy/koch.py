# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 00:31:16 2025

@author: Ala
"""

import turtle
 
def Koch(length, level):
 
    if level== 0:
        turtle.forward(length)
        return
 
    new_length = length / 3.0
    Koch(new_length, level - 1)
    turtle.left(60)
    Koch(new_length, level - 1)
    turtle.right(120)
    Koch(new_length, level -1)
    turtle.left(60)
    Koch(new_length, level -1)
 
 
length = 500.0
 
turtle.speed(0)
turtle.penup()
turtle.goto(-length/2, length/4)
turtle.pendown()
 
for i in range(3):
    Koch(length, 2)
    turtle.right(120)
 
turtle.hideturtle()
turtle.mainloop()