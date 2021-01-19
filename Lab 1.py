import os
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

# state starting health 10-50
def getState():
    return random.randint(10, 50)

class Agent:
    # states
    #00 idle        (*--)
    #01 working     (w++)
    #02 resting     (r++)
    #03 eating      (e++)
    #04 hydrating   (h++)
    #05 socializing (s++)

    #legal-multi-state
    #03+04
    #

    #randomly assigned
    def __init__(self, name):
        self.pos = place()
        self.tag = name
        
        self.w = getState()
        self.c = getState()
        self.s = getState()
        self.e = getState()
        self.d = getState()
        self.f = getState()

    #assigned
##    def __init__(self, name, workplace, consumtion, sleep, eat, drink, friends):
##        self.n = name
##        
##        self.w = workplace
##        self.c = consumtion
##        self.s = sleep
##        self.e = eat
##        self.d = drink
##        self.f = friends

    def get():
        print(self.w, self.c, self.s, self.e, self.d, self.f, sep='\n')
    
    def sleep(cur):
        pass

class Building:
    def __init__(self, location, _tag):
        self.pos = location
        self.tag = _tag

#plane 10x10
Taken = []
for i in range(100):
    Taken += [False]

#places builds or Agents in the game
def place():
    temp = random.randint(0, 99)
    while Taken[temp]:
        temp = random.randint(0, 99)
    Taken[temp] = True
    return temp

#supermarket
B += [Building(place(), "sm")]

#workplace #1
B += [Building(place(), "w1")]

#workplace #2
B += [Building(place(), "w2")]

#Agents
A += [Agent("A")]

A += [Agent("B")]

A += [Agent("C")]

A += [Agent("D")]

#house per agent
for a in A:
    temp = random.randint(0, 99)
    while Taken[temp]:
        temp = random.randint(0, 99)
    Taken[temp] = True

#doing +10
#idle  -1 (for all)

#commands
#p - toggle pause
#s [name] - show state health for [name]
#r [delay] - update game run-delay

#supply agent and places to entity list
def radius(A, B):
    pass

def update(delay):
    time.sleep(delay)
    os.system("cls")

#boot sequence
#update(1) #print state on main thread
#commands(input()) #inputs on seprate thread

for i in range(100):
    if (i / 10 > 0 and i % 10 == 0): print()
    if Taken[i]:
        for a in A:
            if (a.pos == i):
                print(a.tag, end='')
                break
        for b in B:
            if (b.pos == i):
                print(b.tag, end='')
                break
    else:
        print(" ", end='')
