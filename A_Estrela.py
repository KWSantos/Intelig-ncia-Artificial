class State:

    def __init__(self, name : str, h : int):
        self.name = name
        self.opened = None
        self.closed = None
        self.adjacents = []
        self.h = h
        self.g = 0
        self.f = 0
        self.dad = None

    def open(self):
        self.opened = True
        self.closed = False
    
    def close(self):
        self.closed = True
        self.opened = False

def printGraph(graph : list):
    for state in graph:
        print(state.name, end=": [")
        for ad in state.adjacents:
            print(f" {ad[0].name}", end="")
        print(" ]")

def pathToVertex(origin: State, destiny : State):
    if destiny.dad != origin:
        pathToVertex(origin, destiny.dad)
    print(f" -> [{destiny.name}]", end="")

def bestVertex(graph : list):
    menorF = 100
    stateF = None
    print("Nos abertos:", end=" ")
    for i in graph:
        if i.opened and i.f < menorF:
            print(f"[{i.name}]", end=" ")
            menorF = i.f
            stateF = i
    print()
    return stateF

def aStar(graph, initial : State, destiny : State):
    novoF = 0
    initial.f = initial.g + initial.h
    initial.open()
    v = initial
    while v != destiny:
        v = bestVertex(graph)
        print(f"No escolhido: [{v.name}]\n")
        if v == destiny:
            return True
        for u in v.adjacents:
            novoF = v.g + u[1] + u[0].h
            if not ((u[0].closed or u[0].opened) and novoF >= u[0].f):
                u[0].dad = v
                u[0].g = v.g + u[1]
                u[0].f = novoF

                if u[0].closed:
                    u[0].open()
                
                if u[0].opened:
                    u[0].close()

                u[0].open()
        v.close()
    return False


def main():

    f = State("F", 10)
    g = State("G", 10)
    a = State("A", 10)
    b = State("B", 20)
    c = State("C", 10)
    d = State("D", 5)
    e = State("E", 10)
    h = State("H", 0)
    k = State("K", 0)

    f.adjacents.append((g, 15))
    g.adjacents.append((a, 10))
    g.adjacents.append((c, 5))
    a.adjacents.append((d, 10))
    a.adjacents.append((b, 5))
    a.adjacents.append((h, 10))
    b.adjacents.append((f, 5))
    c.adjacents.append((d, 5))
    d.adjacents.append((g, 10))
    d.adjacents.append((e, 5))
    e.adjacents.append((c, 10))
    e.adjacents.append((a, 5))
    e.adjacents.append((k, 10))
    h.adjacents.append((b, 5))
    h.adjacents.append((k, 20))
    k.adjacents.append((b, 10))

    graph = [a, b, c, d, e, f, g, h, k]

    print("Grafo:")
    printGraph(graph)
    print()

    if aStar(graph, g, k):
        print("Caminho: ", end="")
        print(f"[{g.name}]", end="")
        pathToVertex(g, k)
        print("\nCusto total para chegar no No de destino:", k.f)
    else:
        print(f"Nao e possivel partir do vertice {g.name} e ir ao {k.name}")

if __name__=="__main__":
    main()