class Player(Publisher):
    def __init__(self,id):
        self.id = id
        super().__init__()

    def notify(self,value):
        pass #intiliaze
