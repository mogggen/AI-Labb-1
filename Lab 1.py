import Agent
import Building

import turtle
import random
import time

B = [] #Places (Job 1, Job 2, MarketPlace)

#goal: 0 < state < 100


#doing +6
#idle  -1 (for all)

#green supermarket
#blue work
#red job

#destination
def draw(x, y, fillcolor):
    size = 50
    tur = turtle.Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)
    tur.fillcolor(fillcolor)

    #position
    tur.goto(x - size / 2, y - size / 2)
    tur.begin_fill()
    tur.setx(x + size / 2)
    tur.sety(y + size / 2)
    tur.setx(x - size / 2)
    tur.sety(y - size / 2)
    tur.end_fill()
    return (x, y)

market = draw(250, 400, "green")
job = draw(-300, 100, "red")
work = draw(-200, 70, "blue")
home = draw(360, -200, "gray")


#Agents
A = []
A += [Agent('A', "green")]
A += [Agent('B', "red")]
A += [Agent('C', "blue")]
A += [Agent('D', "gray")]

#Buildings
B = [Building(market, "market"),
     Building(job, "job"),
     Building(work, "work"),
     Building(home, "home")]
