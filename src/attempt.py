from route import campus, heuristic_cost

class Node():
    def __init__( self, parent=None, position=None ):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    
def astar( start, end ):
    
    start_node = Node( None, start )
    end_node = Node( None, end )
    
    if start_node != end_node:
        path = []
        
        while start_node is not None:
            path.append( start_node.position )
            start_node = start_node.parent
            
            possible = []
            for paths in campus:
                
                if paths == campus.keys():
                    possible.append( campus )
            
            # Convert values to int
            for val in possible:
                print(val)
            
            # g(n)
            min_g = min( val for val in possible )
            print(min_g)

        # User output
        return path
    
    # Eliminate closed list when start == end
    else:
        return [ start_node.position ]