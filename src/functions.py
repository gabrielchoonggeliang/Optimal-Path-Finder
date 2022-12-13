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
