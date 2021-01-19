import os
import random
import time
import thread
import math

#Final state machine (FSM), Grid

#Samla pengar (jobba), minst 2 olika platser och former.

#Köpa grejer (t ex mat, spade).

#Sova.

#Äta.

#Dricka.

#Umgås med kompisar.

agentsCount = 0

class Agent:
    # state starting health 10-50

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
        self.n = name
        #self.h = 0
        
        self.w = random.randint(10, 50)
        self.c = random.randint(10, 50)
        self.s = random.randint(10, 50)
        self.e = random.randint(10, 50)
        self.d = random.randint(10, 50)
        self.f = random.randint(10, 50)

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
        

#plane 10x10

#market place
mp = random.randint(0, 99)

#house per agent

#workplace #1

#workplace #2

#Agents
A += [Agent("A")]

A += [Agent("B")]

A += [Agent("C")]

A += [Agent("D")]

#doing +10
#idle  -1 (for all)

#commands
#p - toggle pause
#s [name] - show state health for [name]
#r [delay] - update game run-delay

