def getState():
    return random.randint(6, 99)

class Agent:
    #working     (w++)
    #consuming   (c++)
    #socializing (s++)
    #resting     (r++)
    #eating      (e++)
    #hydrating   (h++)

    def __init__(self, name, fillColor):
        self.tur = turtle.Turtle()
        self.tur.speed(4)
        self.tur.fillcolor(fillColor)
        
        self.last = " " #' ' w c s e d f
        
        self.w = getState()
        self.c = getState()
        self.s = getState()
        self.e = getState()
        self.d = getState()
        self.f = getState()

    def get():
        return self.w, self.c, self.s, self.e, self.d, self.f

    def goto(agent, dest):
        agent.towards(dest)
        agent.fd(((agent.tur.xcor() - dest[0])**2 +
                  (agent.tur.ycor() - dest[1])**2)**0.5)
