class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def __repr__(self):
        return format(self.name)
    def __hash__(self):
        return hash(self.name)