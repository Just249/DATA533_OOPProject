class Info_Check():
    
    def __init__(self,input):
        self.list = ["12345","54321"]
        self.input = input
    
    def check_inlist(self):
        if self.input.lower() in self.list:
            return True
        else:
            return False