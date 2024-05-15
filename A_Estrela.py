class Estado:

    def __init__(self, name : str, h : int):
        self.name = name
        self.opened = False
        self.closed = False
        self.adjacents = []
        self.h = h
        self.g = 0
        self.f = 0
        self.dad = None

    def open(self):
        self.opened = True
    
    def close(self):
        self.closed = True
    
    def getAdjacents(self):
        return self.adjacents

def bestVertex(open : set):
    menorF = 100
    stateF = None
    for i in open:
        if i.f < menorF:
            menorF = i.f
            stateF = i
    return stateF

def aEstrela(s : Estado, t : Estado):
    open = set([])
    closed = set([])
    novoF = 0
    s.g = 0
    s.f = s.g + s.h
    v = s
    open.add(s)
    while open != {}:
        v = bestVertex(open)
        print(v.name)
        if v == t:
            return True
        for u in v.adjacents:
            novoF = v.g + u[1] + u[0].h
            
            if not ((u[0] in closed or u[0] in open) and novoF >= u[0].f):
                u[0].dad = v
                u[0].g = v.g + u[1]
                u[0].f = novoF

                if u[0] in closed:
                    closed.remove(u[0])
                
                if u[0] in open:
                    open.remove(u[0])

                open.add(u[0])
        
        open.remove(v)
        closed.add(v)
    return False


def main():

    f = Estado("F", 10)
    g = Estado("G", 10)
    a = Estado("A", 10)
    b = Estado("B", 20)
    c = Estado("C", 10)
    d = Estado("D", 5)
    e = Estado("E", 10)
    h = Estado("H", 0)
    k = Estado("K", 0)

    f.adjacents.append((g, 15))
    f.adjacents.append((b, 5))
    g.adjacents.append((f, 15))
    g.adjacents.append((a, 10))
    g.adjacents.append((d, 10))
    g.adjacents.append((c, 5))
    a.adjacents.append((g, 10))
    a.adjacents.append((d, 10))
    a.adjacents.append((b, 5))
    a.adjacents.append((e, 5))
    a.adjacents.append((h, 10))
    b.adjacents.append((f, 5))
    b.adjacents.append((a, 5))
    b.adjacents.append((h, 5))
    b.adjacents.append((k, 10))
    c.adjacents.append((g, 5))
    c.adjacents.append((d, 5))
    c.adjacents.append((e, 10))
    d.adjacents.append((g, 10))
    d.adjacents.append((a, 10))
    d.adjacents.append((c, 5))
    d.adjacents.append((e, 5))
    e.adjacents.append((c, 10))
    e.adjacents.append((d, 5))
    e.adjacents.append((a, 5))
    e.adjacents.append((k, 10))
    h.adjacents.append((a, 10))
    h.adjacents.append((b, 5))
    h.adjacents.append((k, 20))
    k.adjacents.append((e, 10))
    k.adjacents.append((h, 20))
    k.adjacents.append((b, 10))

    if aEstrela(g, k):
        print("E possivel")
    else:
        print("Nao e possivel")

if __name__=="__main__":
    main()