class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.distance = -1    # for BFS
        self.predecessor = -1 # for BFS
        self.color = "white"  # for BFS
        self.discoveryTime = -1   # for DFS
        self.finishTime = -1      # for DFS

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return (str(self.id) + ' \ndistance: ' + str(self.distance)
               + " \npredecessor " + str(self.predecessor)
               + " \ncolor " + self.color
               + " \ndisc Time " + str(self.discoveryTime)
               + " \nfinish " + str(self.finishTime)
               #+ ' \nconnectedTo: ' + str([x.id for x in self.connectedTo])
               )

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0              # for DFS

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def bfs(g, start):
    vq = []
    distance = 0
    mystart = g.getVertex(start)
    mystart.color = "grey"
    mystart.distance = distance
    mystart.predecessor = None
    vq.append(mystart)
    #print(g.getVertex(start))
    while vq:
        #print(vq)
        curr = vq.pop()
        #print(curr)
        distance += 1
        for c in curr.getConnections():
            if c.color == "white":
                c.predecessor = curr
                c.distance = curr.distance + 1
                c.color = "grey"
                vq.append(c)
        curr.color = "black"

def dfs(g, self):
    for v in g.vertList:
        ve = g.getVertex(v)
        ve.color = "white"
        ve.predecessor = -1
    for v in g.vertList:
        ve = g.getVertex(v)
        if ve.color == "white":
            dfs_visit(ve, g)

def dfs_visit(v: Vertex, g: Graph):
    v.color = "grey"
    g.time += 1
    v.discoveryTime = g.time
    for v_new in v.getConnections():
        #v_new = g.getVertex(c)
        if v_new.color == "white":
            v_new.predecessor = v
            dfs_visit(v_new, g)
    g.time += 1
    v.finishTime = g.time
    v.color = "black"       



g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    print(v)
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))    


g1 = Graph()
for i in range(7):
    g1.addVertex(i)
g1.addEdge(0,1,3)
g1.addEdge(0,2,3)
g1.addEdge(0,4,3)
g1.addEdge(1,5,3)
g1.addEdge(2,3,3)
g1.addEdge(2,4,3)
g1.addEdge(3,6,3)
g1.addEdge(4,6,3)
print("-----------G1---------------")
for v in g1:
    print(v)
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))    
bfs(g1, 0)

print("-----------G1----after bfs---------")
for v in g1:
    print(v)
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))    

g2 = Graph()
for i in range(7):
    g2.addVertex(i)
g2.addEdge(0,1,3)
g2.addEdge(0,2,3)
g2.addEdge(0,4,3)
g2.addEdge(1,5,3)
g2.addEdge(2,3,3)
g2.addEdge(2,4,3)
g2.addEdge(3,6,3)
g2.addEdge(4,6,3)
print("-----------G2---------------")
for v in g2:
    print(v)
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))    
dfs(g2, 0)

print("-----------G2----after dfs---------")
for v in g2:
    print(v)
    #for w in v.getConnections():
    #    print("( %s , %s )" % (v.getId(), w.getId()))    




# From GeeksForGeeks
# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class GraphGfG: 

	# Constructor 
	def __init__(self): 
        # default dictionary to store graph 
	    self.graph = defaultdict(list) 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# Function to print a BFS of graph 
	def BFS(self, s): 

		# Mark all the vertices as not visited 
		visited = [False] * (len(self.graph)) 

		# Create a queue for BFS 
		queue = [] 

		# Mark the source node as 
		# visited and enqueue it 
		queue.append(s) 
		visited[s] = True

		while queue: 
			# Dequeue a vertex from 
			# queue and print it 
			s = queue.pop(0) 
			print (s, end = " ") 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 
			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True

# Driver code 

# Create a graph given in 
# the above diagram 
g = GraphGfG() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
g.BFS(2) 

# This code is contributed by Neelam Yadav 
