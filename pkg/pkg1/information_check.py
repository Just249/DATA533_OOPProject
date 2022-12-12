class Info_Check():
    
    def __init__(self):
        self.list = ["12345678","87654321"]
    
    def check_inlist(self, input):
        if input.lower() in self.list:
            return True