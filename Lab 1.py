import os
import turtle
import random
import time
import threading
import math

#Final state machine (FSM), Grid

#Samla pengar (jobba), minst 2 olika platser och former.

#Köpa grejer (t ex mat, spade).

#Sova.

#Äta.

#Dricka.

#Umgås med kompisar.

A = [] #Agents (Agent A, Agent B, ...)
B = [] #Places (Job 1, Job 2, MarketPlace)

# find a avalible tile to spawn the entity

def getState():
    return random.randint(50, 70)

class Agent:
    # states
    #00 idle        (*--)
    #01 working     (w++)
    #02 resting     (r++)
    #03 eating      (e++)
    #04 hydrating   (h++)
    #05 socializing (s++)

    #legal-multi-state: None

    #randomly assigned
    def __init__(self, name):
        self.x = placeX()
        self.y = placeY()
        self.tag = name
        self.last = " " #' ' w c s e d f
        
        self.w = getState()
        self.c = getState()
        self.s = getState()
        self.e = getState()
        self.d = getState()
        self.f = getState()

    def get():
        print(self.w, self.c, self.s, self.e, self.d, self.f, sep='\n')
    
    def activity():
        last += 6
        pass

class Building:
    def __init__(self, _X, _Y, _tag):
        self.x = place()
        self.y = place()
        self.tag = _tag

#plane 10x10
Taken = []
for i in range(100):
    Taken += [False]

#places builds or Agents in the game
def place():
    temp1 = random.randint(0, 9)
    temp2 = random.randint(0, 9)
    while Taken[temp1 + temp2]:
        temp1 = random.randint(0, 9)
        temp2 = random.randint(0, 9)
    Taken[temp1 + temp2] = True
    return (temp1, temp2)

#supermarket
B += [Building(place(),place(), "sm")]

#workplace #1
B += [Building(place(),place(), "w1")]

#workplace #2
B += [Building(place(),place(), "w2")]

#Agents
for a in range(ord('a'), ord('e')):
    A += [Agent(chr(a))]

#house per agent
for a in A:
    B += [Building(place(), place(), a.tag.upper())]

#doing +10
#idle  -1 (for all)

#commands
#p - toggle pause
#s [name] - show state health for [name]
#r [delay] - update game run-delay

#supply agent and places to entity list
def radius(A, B):
    pass

def drawBuilding():
    build = turtle.turtle()
    global B
    for b in B:
        tur.setx(b.x, b.y)

def update(delay):
    time.sleep(delay)
    os.system("cls")

#boot sequence
#update(1) #print state on main thread
#commands(input()) #inputs on seprate thread


tur = turtle.Turtle()

tur.hide()
tur.begin_fill()


tur.lt(90)
tur.fd(100)
tur.lt(90)
tur.fd(100)
tur.lt(30)
tur.fd(100)
tur.lt(30)
tur.fd(100)
tur.end_fill()
