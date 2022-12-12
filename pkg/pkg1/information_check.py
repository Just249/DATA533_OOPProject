class Info_Check():
    
    def __init__(self,name,iid):
        self.list = ["12345","54321"]
        self.name = name
        self.iid = iid
    
    def check_inlist(self):
        if self.input.lower() in self.list:
            return True
        else:
            return False
        
    def check_name(self):
        if self.name==null:
            return True
        else:
            return False
        
    def check_ID(self):
        if self.iid==null:
            return True
        else:
            return False
    