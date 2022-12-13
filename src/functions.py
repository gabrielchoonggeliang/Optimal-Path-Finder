from sys import exit

# User input class
class UserInput:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def set_start(self, start):
        self.start = start
        
    def set_end(self, end):
        self.end = end
        
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end
    
def answer(list):
    for i in list:
        if i != list[-1]:
            print(i, end=" > ")
        else:
            print(i)

def exit():
    exit(0)