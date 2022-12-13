# A* algorithm

from route import campus, location, heuristic_cost

class Node():
    """A node class for A* Pathfinding"""
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __hash__(self):
        return hash(self.position)


def astar(route, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0  # zero because it's the start node
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0  # zero because it's the end node

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in campus: # Adjacent squares

            # Get node position
            # For example: ("B", "LY3")
            # TODO: find out how to get the position of the node
            node_position = new_position

            # Make sure within range
            if node_position[0] in location.keys():
                continue

            # Create a new node with parent: current_node and position: node_position
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            # TODO: update f, g and h values
            child.g = child.g + 1
            
            child.h = heuristic_cost[child.parent.position]
            
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
