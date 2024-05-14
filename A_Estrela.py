class Estado:

    def __init__(self):
        self.opened = False
        self.closed = False
        self.adjacents = []
        self.h = 0

    def open(self):
        self.opened = True
    
    def close(self):
        self.closed = True
    
    def getAdjacents(self):
        return self.adjacents

def cost(u : Estado, v : Estado):
    if v not in u.adjacents:
        return False
    else:
        i = u.adjacents.index(v)
        return u.adjacents[i][1]
    

def AEstrela(g, s : Estado, t : Estado):
    f = []
    g = []
    dad = []
    open = {}
    closed = {}
    