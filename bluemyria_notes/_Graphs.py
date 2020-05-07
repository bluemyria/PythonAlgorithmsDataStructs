class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.distance = -1    # for BFS
        self.predecessor = -1 # for BFS
        self.color = "white"  # for BFS & DFS
        self.discoveryTime = -1     # for DFS
        self.finishTime = -1        # for DFS

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def setDistance(self, dist=0):
        self.distance = dist
    
    def getDistance(self):
        return self.distance

    def __str__(self):
        return (str(self.id) + ' \ndistance: ' + str(self.distance)
               + " \npredecessor " + str(self.predecessor)
               + " \ncolor " + self.color
               + " \ndisc Time " + str(self.discoveryTime)
               + " \nfinish " + str(self.finishTime)
               #+ ' \nconnectedTo: ' + str([x.id for x in self.connectedTo])
               )
    
    def __lt__(self, other):
        return self.distance < other.getDistance()

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
print('\n\n')

# This code is contributed by Neelam Yadav 



# from Grokking Algorithms & MIT
import collections

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy", 'claire']
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = ['bob']
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def bfs_name(s):
    search_queue = collections.deque()
    search_queue += graph[s]
    # print(search_queue)
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            print('checking: ', person)
            if person_is_seller(person):
                print('found!', person)
            else:
                search_queue += graph[person]
                searched.append(person)
bfs_name('you')
bfs_name('peggy')

print('bfs_name_mit')
# O(V+E)
def bfs_name_mit(start, Adj):
    visited = {start: 0}
    parent = {start: None}
    frontier_nr = 1
    frontier = [start]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if not v in visited:
                    print('checking: ', v)
                    visited[v] = frontier_nr
                    parent[v] = u
                    next.append(v)
        frontier = next
        frontier_nr += 1
    print(visited)
    print(parent)

bfs_name_mit('you', graph)
bfs_name_mit('peggy', graph)


# from MIT & me (mix all interesting aspects from all books)
print ("\n\n***** from MIT & me (mix all interesting aspects from all books) ******") 

def dfs_mit(V, Adj):

    def dfs_visit_mit(s):
        
        nonlocal mytime
        discovery_time[s] = mytime
        color[s] = "grey"
        # process_vertex() if desired
        print('processing.. ', s, 'time: ', mytime)
        mytime += 1
        for v in Adj[s]:  # start v, process_edge() if desired
            print('v, process_edge() ', v)
            if v not in parent:
                parent[v] = s
                dfs_visit_mit(v)
                # finish v
            else: # v in parent
                if color[v] == 'grey':
                    print("-----------------> backward Edge: CYCLE!!!", s, v)
                if color[v] == 'black':
                    if discovery_time[s] < discovery_time[v]:
                        print("-----------------> forward edge: ", s, v)
                    else:
                        print("-----------------> cross edge: ", s, v)
        finish_time[s] = mytime
        color[s] = "black"
        mytime += 1
        
    mytime = 0
    parent = {} 
    discovery_time = {}
    finish_time = {}
    color = {} # make all vertices "white"
    for v in V:
        color[v] = "white"
    
    for s in V:
        if s not in parent: # or check if still white
            parent[s] = None
            dfs_visit_mit(s)

    print('\n\nparent: ', parent)
    print('discovery_time: ', discovery_time)
    print('finish_time: ', finish_time)
    print('color: ', color)
    print('JOB SCHEDULING: ')
    for w in sorted(finish_time, key=finish_time.get, reverse=True):
        print(w, finish_time[w])
    

graph["Mary"] = ["Peter", "Helen"]
graph["Helen"] = ["alice"]
graph["Peter"] = []

print(graph.keys())
print(graph)
dfs_mit(graph.keys(), graph)

# Job scheduling
# Given Directed Acylic Graph (DAG), where vertices represent tasks & edges represent
# dependencies, order tasks without violating dependencies
# run DFS and order in the reverse finish_time
# better to start from vertices w/o incoming edges (not implemented here)
jobsched = {}
jobsched["A"] = ["B", "H"]
jobsched["B"] = ["C"]
jobsched["C"] = ["F"]
jobsched["D"] = ["B", "E"]
jobsched["E"] = ["F"]
jobsched["F"] = []
jobsched["G"] = ["H"]
jobsched["H"] = []
jobsched["I"] = []
print(jobsched.keys())
print(jobsched)
dfs_mit(jobsched.keys(), jobsched)


# Iterative Depth First Search of a Graph // from DSA in Python
def graphDFS(V, Adj, start, goal):
    stack = []
    visited = set()
    stack.append(start)
    
    while stack:
        current = stack.pop()
        visited.add(current)
    
        if current == goal:
            print(visited)
            return True # or return path to goal perhaps
    
        for v in Adj[current]:
            if not v in visited:
                stack.append(v)
    
    return False # or return an empty path
graphDFS(graph.keys(), graph, "Mary", "claire")

import heapq
def dijkstra(aGraph,start):
    pq = []
    start.setDistance(0)
    pq = heapq.heapify([(v.getDistance(),v) for v in aGraph])
    print(pq)
    while pq:
        currentVert = heapq.heappop(pq)
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred( currentVert )
                pq.decreaseKey( nextVert, newDist )


g3 = Graph()
g3.addVertex('u')
g3.addVertex('v')
g3.addVertex('w')
g3.addVertex('x')
g3.addVertex('y')
g3.addVertex('z')
g3.addEdge('u','v',2)
g3.addEdge('u','w',5)
g3.addEdge('u','x',1)
g3.addEdge('v','w',3)
g3.addEdge('v','x',2)
g3.addEdge('x','w',3)
g3.addEdge('x','y',1)
g3.addEdge('w','y',1)
g3.addEdge('w','z',5)
g3.addEdge('y','z',1)
g3.addEdge('v','u',2)
g3.addEdge('w','u',5)
g3.addEdge('x','u',1)
g3.addEdge('w','v',3)
g3.addEdge('x','v',2)
g3.addEdge('w','x',3)
g3.addEdge('y','x',1)
g3.addEdge('y','w',1)
g3.addEdge('z','w',5)
g3.addEdge('z','y',1)
for v in g3:
    print(v)
    for w in v.getConnections():
        print("( %s -> %s, %d )" % (v.getId(), w.getId(), v.getWeight(w)))  
print(g3.getVertices())
print('*************** AFTER DIJKSTRA ***************')
dijkstra(g3, g3.getVertex('u'))
for v in g3:
    print(v)
    for w in v.getConnections():
        print("( %s -> %s, %d )" % (v.getId(), w.getId(), v.getWeight(w)))  


from collections import namedtuple, deque
from pprint import pprint as pp
 
inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class DijkstraGraph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        # pp(self.edges[0])
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}
        # pp(self.vertices)

    def dijkstra(self, source, dest):
        assert source in self.vertices
        
        dist = {vertex: inf for vertex in self.vertices}
        dist[source] = 0
        # pp(dist)

        previous = {vertex: None for vertex in self.vertices}
        # pp(previous)
        
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        # pp(neighbours)
 
        q = self.vertices.copy()
        
        while q:
            # pp(q)
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alternative = dist[u] + cost
                if alternative < dist[v]:       # Relax (u,v,a)
                    dist[v] = alternative
                    previous[v] = u
        # pp(previous)
        sp = deque()
        u = dest
        while previous[u]:
            sp.appendleft(u)
            u = previous[u]
        sp.appendleft(u)
        return sp


mygraph = DijkstraGraph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])
pp(mygraph.dijkstra("a", "e"))
