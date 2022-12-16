# Connects the nodes in the graph to form a route
campus= { "B" : "LY4", "B" : "D4", "B" : "A5", "B" : "A4", "B" : "A3", "B" : "A2", "B" : "A1", "B" : "LY2",  "B" : "LY3",
        "A1" : "M", "A2" : "M","A3" : "M", "A4" : "M", "A5" : "M" , "LY2" : "LY1", "LY3" : "LY1", "LY4" : "LY3",
       "LY2" : "LY3", "LY1" : "LY6", "LY6" : "LY7", "LY6" : "LY3", "LY7" : "LY8", "LY7" : "LY3", "LY3" : "LY8",
        "LY8" : "LY4", "LY8" : "LY9", "LY8" : "LY5", "LY4" : "LY5", "LY5" : "LY9", "LY5" : "D4","LY5" : "D5",
        "D5" : "D4", "D5" : "D6", "D5" : "D3", "D6" : "D2", "D6" : "D3", "D4" : "D3", "D3" : "D2", "D2" : "D1",
        "D3" : "D1", "D4" : "B1", "D3" : "B1", "B1" : "C", "B1" : "A5", "B1" : "S", "D3" : "S", "D1" : "S",
        "C" : "A5", "C" : "F", "F" : "A5" }

# TODO: update the correct values for the nodes
location = { "LY1" : (0, 0), "LY2" : (0, 0), "LY3" : (0, 0), "LY4" : (0, 0), "LY5" : (0, 0), "LY6" : (0, 0), "LY7" : (0, 0), 
            "LY8" : (0, 0), "LY9" : (0, 0), "D1" : (0, 0), "D2" : (0, 0), "D3" : (0, 0), "D4" : (0, 0), "D5" : (0, 0), "D6" : (0, 0),
            "A1" : (0, 0), "A2" : (0, 0), "A3" : (0, 0), "A4" : (0, 0), "A5" : (0, 0), "B" : (0, 0), "B1" : (0, 0), "S" : (0, 0),
            "C" : (0, 0), "F" : (0, 0), "M" : (0, 0)}

heuristic_cost = { "LY1" : 12 , "LY2" : 12, "LY3" : 12, "LY4" : 12, "LY5" : 12, "LY6" : 12,"LY7" : 12,"LY8" : 12,"LY9" : 12, 
       "D1" : 10, "D2" : 10, "D3" : 10, "D4" : 10, "D5" : 10, "D6" : 10, "A1" : 15, "A2" : 15, "A3" : 15, "A4" : 15, 
       "A5" : 15, "B" : 7, "B1" : 19, "S" : 2, "C" : 3, "F" : 8, "M" : 0 } 

path_cost = {}