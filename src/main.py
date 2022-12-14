from model import astar
from functions import UserInput, answer
from route import location

def main():

    current_location = UserInput(" ", " ")
    current_location.set_start(input())
    current_location.set_end(input())
    
    start = current_location.get_start()
    end = current_location.get_end()

    map = location
    global path
    path = astar(map, start, end)
    answer(path)
    

if __name__ == '__main__':
    main()