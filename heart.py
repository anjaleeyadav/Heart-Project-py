import turtle
import math
import turtle
from turtle import *
def hearta(k):
    return 15 * math.sin(k) ** 3
def heartb(k):
    return 12 * math.cos(k) - 5 * \
    math.cos(2 * k) - 5 * \
    math.cos(3 * k) - \
    math.cos(4 * k)
speed(0)
t=turtle.Turtle()
t.write("hello",align="center",font=("Courier",50,"bold"))
speed(200000000000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(1):
        color("red")
        # linewidth=(30)
        # t=turtle.Turtle()
        # t.write("hello",color="red",align="center",font=("Courier",16,"bold",))
    dot()
goto(0,0)
done()

