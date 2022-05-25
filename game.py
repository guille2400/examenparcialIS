import random
class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class Game(Singleton):
    def __init__(self):
        self.players = []
    def randomnumber(self):
        list=[]
        for i in range(5):
            r=random.randint(1,100)
            if r not in list: list.append(r)
        print(""" Numeros random:""")
        for x in range(len(list)):
            print(list[x])
        
    def suscribe(self,strategy):
        self.players.append(strategy)
    def winner(self,value):
        for players in self.players:
            if strategy.winner(value):
                print("won")
                return True
        return False
