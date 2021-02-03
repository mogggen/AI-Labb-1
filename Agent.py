import random
import turtle


def getState(key):
    rand = random.Random()
    return [key, rand.randint(6, 99)]

class Agent:
    #working     (w++)
    #consuming   (c++)
    #eating      (e++)
    #resting     (r++)
    #hydrating   (h++)
    #socializing (s++)

    def __init__(self, name, color):
        
        self.walkspeed = 80
        self.earn = 24
        self.name = name
        self.tur = turtle.Turtle()
        self.tur.speed(0)
        self.tur.pencolor(color)
        self.tur.fillcolor(color)

        self.worst = ["", 100]
        self.last = "r" # w c e h r s

        self.states = [getState("w"),
                       getState("c"),
                       getState("e"),
                       getState("h"),
                       getState("r"),

                       getState("s")]

    #check needs
    def need(self):
        for s in self.states:
            if s[1] < self.worst[1]:
                self.worst = s
    
    def walk(self, dest):
        self.tur.st()
        self.tur.lt(self.tur.towards(dest[0], dest[1]) - self.tur.heading())
        dist = ((self.tur.xcor() - dest[0])**2 +
                (self.tur.ycor() - dest[1])**2)**0.5
        
        if dist > self.walkspeed:
            self.tur.fd(self.walkspeed) #arrive only if destination is within reach
        else:
            self.tur.ht()
            for s in self.states:
                if s[0] == self.worst[0]:
                    s[1] += self.earn
