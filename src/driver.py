from model import astar
from functions import UserInput, answer
from route import location


map  = location

# Reference the values to the dictionary
current_location = UserInput(" ", " ")
current_location.set_start(input())
current_location.set_end(input())

start = current_location.get_start()
end = current_location.get_end()

path = astar(map, start, end)
answer(path)
