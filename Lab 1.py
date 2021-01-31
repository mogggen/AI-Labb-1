import Agent

import turtle
import time

#goal: 0 < state < 100

#doing +6
#idle  -1 (for all)

#green supermarket
#blue work
#red job

print("Staring...")

#destination
def rect(x, y, fillcolor):
    size = 50
    tur = turtle.Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)
    tur.fillcolor(fillcolor)

    #position
    tur.goto(x - size / 2, y - size / 2)

    #fill rec
    tur.begin_fill()
    tur.setx(x + size / 2)
    tur.sety(y + size / 2)
    tur.setx(x - size / 2)
    tur.sety(y - size / 2)
    tur.end_fill()
    
    return (x, y)

#destinations
market = rect(50, 350, "green") #c++ e++
job = rect(150, 80, "red") #w++
park = rect(0, 0, "pink") #s++
work = rect(-200, -70, "blue") #w++
home = rect(40, -170, "gray") #r++ h++

#Agents
A = [Agent.Agent('A', "green"),
     Agent.Agent('B', "red"),
     Agent.Agent('C', "blue"),
     Agent.Agent('D', "yellow")]

def update():
    for a in A:
        for s in a.states:
            s[1] -= 1
            a.need()
        if a.worst[0] == 'r' or a.worst[0] == 'h':
            a.walk(home)
        if a.worst[0] == 'c' or a.worst[0] == 'e':
            a.walk(market)
        if a.worst[0] == 'w':
            if ((a.tur.xcor() - job[0])**2 +
                (a.tur.ycor() - job[1])**2)**0.5 - ((a.tur.xcor() - work[0])**2 +
                (a.tur.ycor() - work[1])**2)**0.5 < 0:
                a.walk (job)
            else:
                a.walk(work)
        if a.worst[0] == 's':
            sms(a)
            a.walk(park)

def sms(a):
    print(a.name, ": Wanna hangout?")
    for i in A:
        if i == a: continue
        
        if i.worst[0] == 's':
            print(i.name, ": Sure! see you at the park in a jiffey")
        else:
            print("sorry, I can't, I'm ",end='')
            if i.worst[0] == 'w':
                print(" working!")
            if i.worst[0] == 'c':
                print(" heading to the store right now")
            if i.worst[0] == 'e':
                print("getting something to eat")
            if i.worst[0] == 'r':
                print("just gonna rest I think, it's been a long day")
            if i.worst[0] == 'h':
                print("thirsty ngl")
            

while True:
    time.sleep(.3)
    update()
