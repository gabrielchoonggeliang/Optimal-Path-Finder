# Connects the nodes in the graph to form a route
campus= { "B" : "LY4", "B" : "D4", "B" : "A5", "B" : "A4", "B" : "A3", "B" : "A2", "B" : "A1", "B" : "LY2",  "B" : "LY3",
        "A1" : "M", "A2" : "M","A3" : "M", "A4" : "M", "A5" : "M" , "LY2" : "LY1", "LY3" : "LY1", "LY4" : "LY3",
       "LY2" : "LY3", "LY1" : "LY6", "LY6" : "LY7", "LY6" : "LY3", "LY7" : "LY8", "LY7" : "LY3", "LY3" : "LY8",
        "LY8" : "LY4", "LY8" : "LY9", "LY8" : "LY5", "LY4" : "LY5", "LY5" : "LY9", "LY5" : "D4","LY5" : "D5",
        "D5" : "D4", "D5" : "D6", "D5" : "D3", "D6" : "D2", "D6" : "D3", "D4" : "D3", "D3" : "D2", "D2" : "D1",
        "D3" : "D1", "D4" : "B1", "D3" : "B1", "B1" : "C", "B1" : "A5", "B1" : "S", "D3" : "S", "D1" : "S",
        "C" : "A5", "C" : "F", "F" : "A5" }

from collections import defaultdict
class Graph:
       def __init__(self):
              self.graph = defaultdict(list)
              
       def addEdge(self,u,v):
              self.graph[u].append(v)

heuristic_cost = { "LY1" : 12 , "LY2" : 12, "LY3" : 12, "LY4" : 12, "LY5" : 12, "LY6" : 12,"LY7" : 12,"LY8" : 12,"LY9" : 12, 
       "D1" : 10, "D2" : 10, "D3" : 10, "D4" : 10, "D5" : 10, "D6" : 10, "A1" : 15, "A2" : 15, "A3" : 15, "A4" : 15, 
       "A5" : 15, "B" : 7, "B1" : 19, "S" : 2, "C" : 3, "F" : 8, "M" : 0 } 

global g
g = Graph()
g.addEdge("B", "LY2")
g.addEdge("B", "LY3")
g.addEdge("B", "LY4")
g.addEdge("B", "D4")
g.addEdge("B", "A5")
g.addEdge("B", "A4")
g.addEdge("B", "A3")
g.addEdge("B", "A2")
g.addEdge("B", "A1")

g.addEdge("LY2", "LY1")
g.addEdge("LY2", "LY3")

g.addEdge("LY3", "LY1")
g.addEdge("LY3", "LY6")
g.addEdge("LY3", "LY7")
g.addEdge("LY3", "LY8")
g.addEdge("LY3", "LY4")

g.addEdge("LY4", "LY3")
g.addEdge("LY4", "LY8")
g.addEdge("LY4", "LY5")

g.addEdge("D4", "LY5")
g.addEdge("D4", "D5")
g.addEdge("D4", "D3")
g.addEdge("D4", " B1")

g.addEdge("A5", "B1")
g.addEdge("A5", "C")
g.addEdge("A5", "F")
g.addEdge("A5", "M")
g.addEdge("A5", "A4")

g.addEdge("A4", "A5")
g.addEdge("A4", "M")
g.addEdge("A4", "A3")

g.addEdge("A3", "A4")
g.addEdge("A3", "M")
g.addEdge("A3", "A2")

g.addEdge("A2", "A3")
g.addEdge("A2", "M")
g.addEdge("A2", "A1")

g.addEdge("A1", "A2")
g.addEdge("A1", "M")

g.addEdge("LY1", "LY6")
g.addEdge("LY1", "LY3")

g.addEdge("LY6", "LY1")
g.addEdge("LY6", "LY7")
g.addEdge("LY6", "LY3")

g.addEdge("LY7", "LY6")
g.addEdge("LY7", "LY8")
g.addEdge("LY7", "LY3")

g.addEdge("LY8", "LY7")
g.addEdge("LY8", "LY3")
g.addEdge("LY8", "LY4")
g.addEdge("LY8", "LY5")

g.addEdge("LY5", "LY8")
g.addEdge("LY5", "LY4")
g.addEdge("LY5", "LY9")
g.addEdge("LY5", "D5")
g.addEdge("LY5", "D4")

g.addEdge("LY9", "LY5")
g.addEdge("LY9", "LY8")

g.addEdge("D5", "LY5")
g.addEdge("D5", "D4")
g.addEdge("D5", "D6")
g.addEdge("D5", "D3")

g.addEdge("D6", "D5")
g.addEdge("D6", "D2")
g.addEdge("D6", "D3")

g.addEdge("D3", "D6")
g.addEdge("D3", "D2")
g.addEdge("D3", "D1")
g.addEdge("D3", "B1")
g.addEdge("D3", "D4")

g.addEdge("D2", "D6")
g.addEdge("D2", "D3")
g.addEdge("D2", "D1")

g.addEdge("D1", "D2")
g.addEdge("D1", "D3")
g.addEdge("D1", "S")

g.addEdge("B1", "D3")
g.addEdge("B1", "D4")
g.addEdge("B1", "A5")
g.addEdge("B1", "C")

g.addEdge("S", "D1")
g.addEdge("S", "D3")

g.addEdge("C", "B1")
g.addEdge("C", "A5")
g.addEdge("C", "F")

g.addEdge("F", "C")
g.addEdge("F", "A5")

g.addEdge("M", "A5")
g.addEdge("M", "A4")
g.addEdge("M", "A3")
g.addEdge("M", "A2")
g.addEdge("M", "A1")

g.addEdge("A5", "B")

g.addEdge("A4", "B")

g.addEdge("A3", "B")

g.addEdge("A2", "B")

g.addEdge("A1", "B")

g.addEdge("LY2", "B")

g.addEdge("LY3", "B")

g.addEdge("LY4", "B")

g.addEdge("D4", "B")

path_cost = {}