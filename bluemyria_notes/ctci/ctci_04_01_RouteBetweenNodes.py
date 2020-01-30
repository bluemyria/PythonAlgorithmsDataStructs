from pprint import pprint
from queue import Queue

class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getId(self):
        return self.id
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph():
    def __init__(self):
        self.nr_vertices = 0
        self.vertices = {}

    def addVertex(self, key):
        self.nr_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def getVertex(self, key):
        if key in self.vertices.keys():
            return self.vertices[key]
        else:
            return None
    
    def getVerticesKeys(self):
        return self.vertices.keys()

    def getVertices(self):
        return self.vertices.values()
    

    def __contains__(self, v):
        return v in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def addEdge(self, v1, v2, weight = 0):
        if not v1 in self.vertices:
            self.addVertex(v1)
        if not v2 in self.vertices:
            self.addVertex(v2)

        self.vertices[v1].addNeighbor(self.vertices[v2], weight)
    

def breadthfirstsearch(g, start, end):
    q = Queue()
    visited = {}

    if start == end:
        return True
    
    for key in g.getVerticesKeys():
        visited[key] = False
    
    visited[start] = False
    q.put(start)

    while not q.empty():
        vk = q.get()
        if vk != None and not visited[vk]:
            v = g.getVertex(vk)
            if v != None:
                for kch in v.getConnections():                
                    if kch.id == end:
                        return True
                    q.put(kch.id)
            visited[vk] = True
    return False


def breadthfirstsearchRec(g, start, end, path=[]):
    pass

g = Graph()
for i in range(6):
    g.addVertex(i)
pprint(g.vertices)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
g.addEdge(5,6,1)
for v in g:
    # pprint(v.connectedTo)
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

if breadthfirstsearch(g, 0, 4):
    print("0, 4, True")
else:
    print("0, 4, False")
if breadthfirstsearch(g, 0, 3):
    print("0, 3, True")
else:
    print("0, 3, False")
if breadthfirstsearch(g, 1, 4):
    print("1, 4, True")
else:
    print("1, 4, False")
if breadthfirstsearch(g, 3, 1):
    print("3, 1, True")
else:
    print("3, 1, False")

if breadthfirstsearch(g, 6, 1):
    print("6, 1, True")
else:
    print("6, 1, False")