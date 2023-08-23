import turtle
from random import randint
import time
Wn=turtle.Screen()
Wn.bgcolor("light blue")

Ugur=turtle.Turtle("turtle")
Ugur.shapesize(stretch_wid=2, stretch_len=2, outline=1)
Ugur.speed(1)

pen = turtle.Turtle(visible=False)
pen.penup()
pen.goto(-150, 400)
pen.lives = 0
pen.font = ("Arial", 30, "normal")
pen.speed(0)

#
#
#
'''
saat=turtle.Turtle()
saat.penup()
saat.goto(-150,300)
saat.times=30


def fonk():
  saat.clear()
  saat.times-=1
  saat.write(f"Score: {saat.times}", font=pen.font)
while(saat.times>0):
  Wn.ontimer(fonk, 10)
if saat.times==0:
  saat.write("Game Over")
'''
#
def onclick_high(x, a):
  pen.clear()
  pen.lives += 1
  pen.write(f"Score: {pen.lives}", font=pen.font)


Ugur.onclick(onclick_high)





while(True):
  Ugur.penup()
  a=randint(-450,450)
  b=randint(-450,450)
  Ugur.goto(a,b)








Wn.mainloop()